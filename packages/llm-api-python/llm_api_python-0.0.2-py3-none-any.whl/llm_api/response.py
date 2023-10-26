"""a wrapper object for API responses"""
from typing import Optional


class LlmApiResponse:
    """A representation class for responses from llm-api"""

    def __init__(self, data, headers):
        self._headers = headers
        self.data = data

    @property
    def request_id(self) -> Optional[str]:
        """request-id response headers"""
        return self._headers.get("request-id")

    @property
    def retry_after(self) -> Optional[int]:
        """retry-after response header"""
        try:
            return int(self._headers.get("retry-after"))
        except TypeError:
            return None

    @property
    def operation_location(self) -> Optional[str]:
        """operation-location response header"""
        return self._headers.get("operation-location")

    @property
    def organization(self) -> Optional[str]:
        """OpenAI-Organization response header"""
        return self._headers.get("OpenAI-Organization")

    @property
    def response_ms(self) -> Optional[int]:
        """Openai-Processing-Ms response header"""
        h = self._headers.get("Openai-Processing-Ms")
        return None if h is None else round(float(h))
