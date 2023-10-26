"""LLM API models client."""
import os
from contextvars import ContextVar
from typing import Callable, Optional, Union

import requests
from aiohttp import ClientSession

from llm_api.completion import ChatCompletion
from llm_api.error import APIError, InvalidRequestError, LlmApiError  # noqa: F401

__all__ = ["ChatCompletion"]

api_key = os.environ.get("LLM_API_API_KEY")
api_key_path: Optional[str] = os.environ.get("LLM_API_API_KEY_PATH")

api_base = os.environ.get("LLM_API_API_BASE", "http://localhost:8000")

requestssession: Optional[
    Union["requests.Session", Callable[[], "requests.Session"]]
] = None

aiosession: ContextVar[Optional["ClientSession"]] = ContextVar(
    "aiohttp-session", default=None
)
