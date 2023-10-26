"""utils"""
import time
from typing import Any

import llm_api
from llm_api import error
from llm_api.response import LlmApiResponse


def default_api_key() -> str:
    """read the configured api key from env var or a configured file"""
    if llm_api.api_key_path:
        with open(llm_api.api_key_path, "rt", encoding="utf-8") as k:
            api_key = k.read().strip()
            return api_key
    if llm_api.api_key is not None:
        return llm_api.api_key

    raise error.AuthenticationError(
        "No API key provided. You can set your API key in code using"
        " 'llm_api.api_key = <API-KEY>', or you can set the environment variable"
        " LLMAPI_API_KEY=<API-KEY>. If your API key is stored in a file,"
        " you can point the llm_api module at it with 'llm_api.api_key_path = <PATH>'."
    )


def convert_to_llm_object(resp, api_key=None):
    """convert to LLMObject"""
    from llm_api.llm_object import LLMObject  # pylint: disable=import-outside-toplevel

    if isinstance(resp, LlmApiResponse):
        resp = resp.data

    if isinstance(resp, list):
        return [convert_to_llm_object(i, api_key) for i in resp]
    if isinstance(resp, dict) and not isinstance(resp, LLMObject):
        resp = resp.copy()

        return LLMObject.construct_from(
            resp,
            api_key,
        )

    return resp


def wrap_text_with_openai_format(text: str) -> Any:
    """to comply with openai, wrap the response with openai response structure"""
    return {
        "id": None,
        "object": "chat.completion",
        "created": int(time.time()),
        "model": None,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": text,
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": None,
            "completion_tokens": None,
            "total_tokens": None,
        },
    }
