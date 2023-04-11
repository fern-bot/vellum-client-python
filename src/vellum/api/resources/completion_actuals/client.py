# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
import uuid
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.internal_server_error import InternalServerError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.types.error_response import ErrorResponse
from .types.submit_completion_actual_request import SubmitCompletionActualRequest


class CompletionActualsClient:
    def __init__(self, *, environment: str, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def submit(
        self,
        *,
        deployment_id: typing.Optional[uuid.UUID] = None,
        deployment_name: typing.Optional[str] = None,
        actuals: typing.List[SubmitCompletionActualRequest],
    ) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "v1/submit-completion-actuals"),
            json=jsonable_encoder(
                {"deployment_id": deployment_id, "deployment_name": deployment_name, "actuals": actuals}
            ),
            headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCompletionActualsClient:
    def __init__(self, *, environment: str, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def submit(
        self,
        *,
        deployment_id: typing.Optional[uuid.UUID] = None,
        deployment_name: typing.Optional[str] = None,
        actuals: typing.List[SubmitCompletionActualRequest],
    ) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "v1/submit-completion-actuals"),
                json=jsonable_encoder(
                    {"deployment_id": deployment_id, "deployment_name": deployment_name, "actuals": actuals}
                ),
                headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise NotFoundError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 400:
            raise InternalServerError(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
