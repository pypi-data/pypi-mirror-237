"""llm-api base object ported from the OpenAI python lib"""
import asyncio
import json
import threading
import time
from contextlib import asynccontextmanager
from enum import Enum
from json import JSONDecodeError
from typing import AsyncGenerator, AsyncIterator, Dict, Iterator, Optional, Tuple, Union
from urllib.parse import urlencode, urlsplit, urlunsplit

import aiohttp
import requests

import llm_api
from llm_api import error, util
from llm_api.response import LlmApiResponse

TIMEOUT_SECS = 600
MAX_SESSION_LIFETIME_SECS = 180
MAX_CONNECTION_RETRIES = 3

_thread_context = threading.local()


class AuthType(Enum):
    """Enum class for authentication type"""

    Bearer = 1
    ApiKey = 2


def _make_session() -> requests.Session:
    """create a new requests session"""
    if llm_api.requestssession:
        if isinstance(llm_api.requestssession, requests.Session):
            return llm_api.requestssession
        return llm_api.requestssession()  # pylint: disable=not-callable
    s = requests.Session()

    s.mount(
        "https://",
        requests.adapters.HTTPAdapter(max_retries=MAX_CONNECTION_RETRIES),
    )
    return s


@asynccontextmanager
async def aiohttp_session() -> AsyncIterator[aiohttp.ClientSession]:
    """create an aiohttp aasync session"""
    user_set_session = llm_api.aiosession.get()
    if user_set_session:
        yield user_set_session
    else:
        async with aiohttp.ClientSession() as session:
            yield session


def parse_stream_helper(line: bytes) -> Optional[str]:
    """a helper for parsing stream content"""
    if line:
        if line.strip() == b"data: [DONE]":
            return None
        if line.startswith(b"data: "):
            line = line[len(b"data: ") :]
            return line.decode("utf-8")
    return None


def _build_api_url(url, query):
    """build api url"""
    scheme, netloc, path, base_query, fragment = urlsplit(url)

    if base_query:
        query = f"{base_query}&{query}"

    return urlunsplit((scheme, netloc, path, query, fragment))


def parse_stream(rbody: Iterator[bytes]) -> Iterator[str]:
    """parse the content of stream response"""
    for line in rbody:
        _line = parse_stream_helper(line)
        if _line is not None:
            yield _line


async def parse_stream_async(rbody: aiohttp.StreamReader):
    """parse the content of stream aiohttp response"""
    async for line in rbody:
        _line = parse_stream_helper(line)
        if _line is not None:
            yield _line


class ApiObject(dict):
    """llm-api base object"""

    def __init__(
        self,
        api_key=None,
        api_base=None,
        auth_type=AuthType.Bearer,
        **params,
    ):
        super().__init__()
        self._retrieve_params = params

        object.__setattr__(self, "api_key", api_key or util.default_api_key())
        object.__setattr__(self, "api_base", api_base or llm_api.api_base)
        object.__setattr__(self, "auth_type", auth_type)

    def _prepare_request_raw(
        self,
        url,
        supplied_headers,
        method,
        params,
    ) -> Tuple[str, Dict[str, str], Optional[bytes]]:
        """prepares a requests request"""
        abs_url = f"{self.api_base}{url}"
        data = None
        headers = {"User-Agent": "LLM-API Python/0.0.1"}
        if method in ("get", "delete"):
            if params:
                encoded_params = urlencode(
                    [(k, v) for k, v in params.items() if v is not None]
                )
                abs_url = _build_api_url(abs_url, encoded_params)
        elif method in {"post", "put"}:
            if params:
                data = json.dumps(params).encode()
                headers["Content-Type"] = "application/json"
        else:
            raise error.APIConnectionError(f"Unrecognized HTTP method {method}.")

        if self.auth_type == AuthType.Bearer:
            headers["Authorization"] = f"Bearer {self.api_key}"
        else:
            headers["api-key"] = self.api_key

        headers.update(supplied_headers or {})

        return abs_url, headers, data

    def request_raw(
        self,
        method,
        url,
        params=None,
        headers=None,
        stream=False,
        request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> requests.Response:
        """request to llm-api"""
        if params is None:
            params = self._retrieve_params

        abs_url, headers, data = self._prepare_request_raw(url, headers, method, params)

        if not hasattr(_thread_context, "session"):
            _thread_context.session = _make_session()
            _thread_context.session_create_time = time.time()
        elif (
            time.time() - getattr(_thread_context, "session_create_time", 0)
            >= MAX_SESSION_LIFETIME_SECS
        ):
            _thread_context.session.close()
            _thread_context.session = _make_session()
            _thread_context.session_create_time = time.time()
        try:
            result = _thread_context.session.request(
                method,
                abs_url,
                headers=headers,
                data=data,
                stream=stream,
                timeout=request_timeout if request_timeout else TIMEOUT_SECS,
            )
        except requests.exceptions.Timeout as e:
            raise error.Timeout(f"Request timed out: {e}") from e
        except requests.exceptions.RequestException as e:
            raise error.APIConnectionError(
                f"Error communicating with llm-api: {e}"
            ) from e
        return result

    def handle_error_response(self, rbody, rcode, resp, rheaders, stream_error=False):
        """handle differnt error API responses"""
        try:
            error_data = resp["detail"]
        except (KeyError, TypeError) as exc:
            raise error.APIError(
                f"Invalid response object from API: {rbody} (HTTP response code "
                f"was {rcode})",
                rbody,
                rcode,
                resp,
            ) from exc

        if isinstance(error_data, list):
            err_msg = "\n".join(
                [
                    f"{error_item.get('msg')} {error_item.get('loc')}"
                    f" type: {error_item.get('type')}"
                    for error_item in error_data
                ]
            )
        else:
            err_msg = error_data

        # Rate limits were previously coded as 400's with code 'rate_limit'
        if rcode == 429:
            return error.RateLimitError(err_msg, rbody, rcode, resp, rheaders)
        if rcode in [400, 404, 415]:
            return error.InvalidRequestError(err_msg, rbody, rcode, resp, rheaders)
        if rcode == 401:
            return error.AuthenticationError(err_msg, rbody, rcode, resp, rheaders)
        if rcode == 403:
            return error.PermissionError(err_msg, rbody, rcode, resp, rheaders)
        if rcode == 409:
            return error.TryAgain(err_msg, rbody, rcode, resp, rheaders)
        if stream_error:
            parts = [
                err_msg,
                "(Error occurred while streaming.)",
            ]
            message = " ".join([p for p in parts if p is not None])
            return error.APIError(message, rbody, rcode, resp, rheaders)

        return error.APIError(
            f"{err_msg} {rbody} {rcode} {resp} {rheaders}",
            rbody,
            rcode,
            resp,
            rheaders,
        )

    def _interpret_response_line(
        self, rbody: str, rcode: int, rheaders, stream: bool
    ) -> LlmApiResponse:
        # HTTP 204 response code does not have any content in the body.
        if rcode == 204:
            return LlmApiResponse(None, rheaders)

        if rcode == 503:
            raise error.ServiceUnavailableError(
                "The server is overloaded or not ready yet.",
                rbody,
                rcode,
                headers=rheaders,
            )
        try:
            # LLM-API returns plain text
            if "text/plain" in rheaders.get(
                "Content-Type", ""
            ) or "text/event-stream" in rheaders.get("Content-Type", ""):
                data = rbody
            elif isinstance(rbody, str):
                data = util.wrap_text_with_openai_format(rbody)
            else:
                data = json.loads(rbody)
        except (JSONDecodeError, UnicodeDecodeError) as e:
            raise error.LlmApiError(
                f"HTTP code {rcode} from API ({rbody})",
                rbody,
                rcode,
                headers=rheaders,
            ) from e
        resp = LlmApiResponse(data, rheaders)
        # In the future, we might add a "status" parameter to errors
        # to better handle the "error while streaming" case.
        stream_error = stream and "error" in resp.data
        if stream_error or not 200 <= rcode < 300:
            raise self.handle_error_response(
                rbody, rcode, resp.data, rheaders, stream_error=stream_error
            )
        return resp

    def _interpret_response(
        self, result: requests.Response, stream: bool
    ) -> Tuple[Union[LlmApiResponse, Iterator[LlmApiResponse]], bool]:
        """Returns the response(s) and a bool indicating whether it is a stream."""
        if stream and "text/event-stream" in result.headers.get("Content-Type", ""):
            return (
                self._interpret_response_line(
                    line, result.status_code, result.headers, stream=True
                )
                for line in parse_stream(result.iter_lines())
            ), True

        return (
            self._interpret_response_line(
                result.content.decode("utf-8"),
                result.status_code,
                result.headers,
                stream=False,
            ),
            False,
        )

    async def _interpret_async_response(
        self, result: aiohttp.ClientResponse, stream: bool
    ) -> Tuple[Union[LlmApiResponse, AsyncGenerator[LlmApiResponse, None]], bool]:
        """Returns the response(s) and a bool indicating whether it is a stream."""
        if stream and "text/event-stream" in result.headers.get("Content-Type", ""):
            return (
                self._interpret_response_line(
                    line, result.status, result.headers, stream=True
                )
                async for line in parse_stream_async(result.content)
            ), True

        try:
            await result.read()
        except (aiohttp.ServerTimeoutError, asyncio.TimeoutError) as e:
            raise error.Timeout("Request timed out") from e
        except aiohttp.ClientError:
            # util.log_warn(e, body=result.content)
            pass
        return (
            self._interpret_response_line(
                (await result.read()).decode("utf-8"),
                result.status,
                result.headers,
                stream=False,
            ),
            False,
        )

    async def arequest_raw(
        self,
        method,
        url,
        session,
        *,
        params=None,
        headers: Optional[Dict[str, str]] = None,
        request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> aiohttp.ClientResponse:
        """send request"""
        abs_url, headers, data = self._prepare_request_raw(url, headers, method, params)

        if isinstance(request_timeout, tuple):
            timeout = aiohttp.ClientTimeout(
                connect=request_timeout[0],
                total=request_timeout[1],
            )
        else:
            timeout = aiohttp.ClientTimeout(
                total=request_timeout if request_timeout else TIMEOUT_SECS
            )

        request_kwargs = {
            "method": method,
            "url": abs_url,
            "headers": headers,
            "data": data,
            "timeout": timeout,
        }

        try:
            result = await session.request(**request_kwargs)

            return result
        except (aiohttp.ServerTimeoutError, asyncio.TimeoutError) as e:
            raise error.Timeout("Request timed out") from e
        except aiohttp.ClientError as e:
            raise error.APIConnectionError("Error communicating with llm-api") from e

    def request(
        self,
        method,
        url,
        params=None,
        headers=None,
        stream: bool = False,
        request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> Tuple[Union[LlmApiResponse, Iterator[LlmApiResponse]], bool, str]:
        """send request"""
        result = self.request_raw(
            method.lower(),
            url,
            params=params,
            headers=headers,
            stream=stream,
            request_timeout=request_timeout,
        )
        resp, got_stream = self._interpret_response(result, stream)
        return resp, got_stream, self.api_key

    async def arequest(
        self,
        method,
        url,
        params=None,
        headers=None,
        stream: bool = False,
        request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> Tuple[Union[LlmApiResponse, AsyncGenerator[LlmApiResponse, None]], bool, str]:
        """send request and process result"""
        ctx = aiohttp_session()
        session = await ctx.__aenter__()
        try:
            result = await self.arequest_raw(
                method.lower(),
                url,
                session,
                params=params,
                headers=headers,
                request_timeout=request_timeout,
            )
            resp, got_stream = await self._interpret_async_response(result, stream)
        except Exception:
            await ctx.__aexit__(None, None, None)
            raise
        if got_stream:

            async def wrap_resp():
                assert isinstance(resp, AsyncGenerator)
                try:
                    async for r in resp:
                        yield r
                finally:
                    await ctx.__aexit__(None, None, None)

            return wrap_resp(), got_stream, self.api_key

        await ctx.__aexit__(None, None, None)
        return resp, got_stream, self.api_key
