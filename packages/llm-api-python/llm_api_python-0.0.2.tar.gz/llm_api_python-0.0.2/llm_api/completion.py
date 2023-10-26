"""
llm-api model client implementation
"""

from llm_api import util
from llm_api.api_object import ApiObject
from llm_api.response import LlmApiResponse

MAX_TIMEOUT = 20

DEFAULT_PROMPT = "You are a helpful assistant."


class ChatCompletion(ApiObject):
    """A wrapper for LLM API client completion."""

    @classmethod
    def __prepare_prompt(cls, **params):
        """this translates OpenAI's `messages` param to
        LLM-API's `prompt` param. Still `prompt` takes precedence"""
        if "messages" in params and "prompt" not in params:
            messages = params.get("messages")
            prompt = DEFAULT_PROMPT
            context_parts = []
            full_prompt = ""

            for message in messages:
                if "role" in message and message.get("role").lower == "system":
                    prompt = message.get("content")

                context_parts.append(
                    f"## {message.get('role', 'user')}: {message.get('content')}"
                )
            full_prompt = "\n".join(context_parts)
            full_prompt = "\n".join([prompt, full_prompt, "## assistant:"])
            return full_prompt
        return params.get("prompt")

    @classmethod
    def __prepare_create_request(
        cls,
        api_key=None,
        api_base=None,
        **params,
    ):
        timeout = params.pop("timeout", None)
        stream = params.get("stream", False)
        headers = params.pop("headers", None)
        request_timeout = params.pop("request_timeout", None)

        if timeout is None:
            # No special timeout handling
            pass
        elif timeout > 0:
            params["timeout"] = min(timeout, MAX_TIMEOUT)
            timeout = (timeout - params["timeout"]) or None
        elif timeout == 0:
            params["timeout"] = MAX_TIMEOUT

        requester = ApiObject(
            api_key,
            api_base=api_base,
        )

        params["prompt"] = cls.__prepare_prompt(**params)

        return (
            timeout,
            stream,
            headers,
            request_timeout,
            requester,
            params,
        )

    @classmethod
    def create(
        cls,
        api_key=None,
        api_base=None,
        **params,
    ):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://github.com/1b5d/llm-api-python
        for a list of valid parameters.
        """

        (
            timeout,
            stream,
            headers,
            request_timeout,
            requester,
            params,
        ) = cls.__prepare_create_request(api_key=api_key, api_base=api_base, **params)

        response, _, api_key = requester.request(
            "post",
            "/agenerate" if stream else "/generate",
            params=params,
            headers=headers,
            stream=stream,
            request_timeout=request_timeout,
        )

        if stream:
            # must be an iterator
            assert not isinstance(response, LlmApiResponse)
            return (
                util.convert_to_llm_object(
                    line,
                    api_key,
                )
                for line in response
            )

        obj = util.convert_to_llm_object(
            response,
            api_key,
        )

        if timeout is not None:
            obj.wait(timeout=timeout or None)

        return obj

    @classmethod
    async def acreate(cls, api_key=None, api_base=None, **params):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://github.com/1b5d/llm-api-python
        for a list of valid parameters.
        """
        (
            timeout,
            stream,
            headers,
            request_timeout,
            requester,
            params,
        ) = cls.__prepare_create_request(api_key=api_key, api_base=api_base, **params)

        response, _, api_key = await requester.arequest(
            "post",
            "/agenerate" if stream else "/generate",
            params=params,
            headers=headers,
            stream=stream,
            request_timeout=request_timeout,
        )

        if stream:
            # must be an iterator
            assert not isinstance(response, LlmApiResponse)
            return (
                util.convert_to_llm_object(
                    line,
                    api_key,
                )
                async for line in response
            )

        obj = util.convert_to_llm_object(
            response,
            api_key,
        )

        if timeout is not None:
            await obj.await_(timeout=timeout or None)

        return obj
