"""LLM object"""
import json
from copy import deepcopy
from typing import Optional, Tuple, Union

from llm_api import util
from llm_api.api_object import ApiObject
from llm_api.response import LlmApiResponse


class LLMObject(dict):
    """LLM object"""

    api_base_override = None

    def __init__(
        self,
        api_key=None,
        api_base=None,
        **params,
    ):
        super().__init__()

        self._retrieve_params = params

        object.__setattr__(self, "api_key", api_key)
        object.__setattr__(self, "api_base_override", api_base)

    def __setattr__(self, k, v):
        if k[0] == "_" or k in self.__dict__:
            return super().__setattr__(k, v)

        self[k] = v
        return None

    def __getattr__(self, k):
        if k[0] == "_":
            raise AttributeError(k)
        try:
            return self[k]
        except KeyError as err:
            raise AttributeError(*err.args) from err

    def __delattr__(self, k):
        if k[0] == "_" or k in self.__dict__:
            super().__delattr__(k)
        else:
            del self[k]

    def __setitem__(self, k, v):
        if v == "":
            raise ValueError(
                f"You cannot set {k} to an empty string. "
                f"We interpret empty strings as None in requests."
                f"You may set {str(self)}.{k} = None to delete the property"
            )
        super().__setitem__(k, v)

    def __delitem__(self, k):
        raise NotImplementedError("del is not supported")

    def __setstate__(self, state):
        self.update(state)

    def __reduce__(self):
        reduce_value = (
            type(self),  # callable
            (self.api_key,),  # args
            dict(self),  # state
        )
        return reduce_value

    @classmethod
    def construct_from(
        cls,
        values,
        api_key: Optional[str] = None,
    ):
        """construct LLMObject from values"""
        instance = cls(
            api_key=api_key,
        )
        instance.refresh_from(
            values,
            api_key=api_key,
        )
        return instance

    def refresh_from(
        self,
        values,
        api_key=None,
    ):
        """update LLMObject from values"""
        self.api_key = (  # pylint: disable=attribute-defined-outside-init
            api_key or getattr(values, "api_key", None)
        )

        # Wipe old state before setting new.
        self.clear()
        for k, v in values.items():
            super().__setitem__(k, util.convert_to_llm_object(v, api_key))

        self._previous = values  # pylint: disable=attribute-defined-outside-init

    @classmethod
    def api_base(cls):
        """api-base"""
        return None

    def request(
        self,
        method,
        url,
        params=None,
        headers=None,
        stream=False,
        request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ):
        """send request"""
        if params is None:
            params = self._retrieve_params
        requestor = ApiObject(
            key=self.api_key,
            api_base=self.api_base_override or self.api_base(),
        )
        response, stream, api_key = requestor.request(
            method,
            url,
            params=params,
            stream=stream,
            headers=headers,
            request_timeout=request_timeout,
        )

        if stream:
            assert not isinstance(response, LlmApiResponse)  # must be an iterator
            return (util.convert_to_llm_object(line, api_key) for line in response)

        return util.convert_to_llm_object(
            response,
            api_key,
        )

    async def arequest(
        self,
        method,
        url,
        params=None,
        headers=None,
        stream=False,
        request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ):
        """send request"""
        if params is None:
            params = self._retrieve_params
        requestor = ApiObject(
            key=self.api_key,
            api_base=self.api_base_override or self.api_base(),
        )
        response, stream, api_key = await requestor.arequest(
            method,
            url,
            params=params,
            stream=stream,
            headers=headers,
            request_timeout=request_timeout,
        )

        if stream:
            assert not isinstance(response, LlmApiResponse)  # must be an iterator
            return (
                util.convert_to_llm_object(
                    line,
                    api_key,
                )
                for line in response
            )

        return util.convert_to_llm_object(
            response,
            api_key,
        )

    def __repr__(self):
        ident_parts = [type(self).__name__]

        obj = self.get("object")
        if isinstance(obj, str):
            ident_parts.append(obj)

        if isinstance(self.get("id"), str):
            ident_parts.append(f"id={self.get('id')}")

        return f"<{' '.join(ident_parts)} at {hex(id(self))}> JSON: {str(self)}"

    def __str__(self):
        obj = self.to_dict_recursive()
        return json.dumps(obj, indent=2)

    def to_dict(self):
        """convert to regular dict"""
        return dict(self)

    def to_dict_recursive(self):
        """convert to regular dict recursive"""
        d = dict(self)
        for k, v in d.items():
            if isinstance(v, LLMObject):
                d[k] = v.to_dict_recursive()
            elif isinstance(v, list):
                d[k] = [
                    e.to_dict_recursive() if isinstance(e, LLMObject) else e for e in v
                ]
        return d

    def __copy__(self):
        copied = LLMObject(self.api_key, self.api_base_override)

        copied._retrieve_params = self._retrieve_params

        for k, v in self.items():
            super().__setitem__(k, v)

        return copied

    def __deepcopy__(self, memo):
        copied = self.__copy__()
        memo[id(self)] = copied

        for k, v in self.items():
            super().__setitem__(k, deepcopy(v, memo))

        return copied
