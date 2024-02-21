# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...types.named_test_case_variable_value_request import NamedTestCaseVariableValueRequest
from ...types.test_suite_test_case import TestSuiteTestCase

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TestSuitesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upsert_test_suite_test_case(
        self,
        id: str,
        *,
        upsert_test_suite_test_case_request_id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        input_values: typing.List[NamedTestCaseVariableValueRequest],
        evaluation_values: typing.List[NamedTestCaseVariableValueRequest],
    ) -> TestSuiteTestCase:
        """
        Upserts a new test case for a test suite, keying off of the optionally provided test case id.

        If an id is provided and has a match, the test case will be updated. If no id is provided or no match
        is found, a new test case will be appended to the end.

        Note that a full replacement of the test case is performed, so any fields not provided will be removed
        or overwritten with default values.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - upsert_test_suite_test_case_request_id: typing.Optional[str].

            - label: typing.Optional[str].

            - input_values: typing.List[NamedTestCaseVariableValueRequest].

            - evaluation_values: typing.List[NamedTestCaseVariableValueRequest].
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suites.upsert_test_suite_test_case(
            id="id",
            input_values=[],
            evaluation_values=[],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"input_values": input_values, "evaluation_values": evaluation_values}
        if upsert_test_suite_test_case_request_id is not OMIT:
            _request["id"] = upsert_test_suite_test_case_request_id
        if label is not OMIT:
            _request["label"] = label
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", f"v1/test-suites/{id}/test-cases"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TestSuiteTestCase, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_test_suite_test_case(self, id: str, test_case_id: str) -> None:
        """
        Deletes an existing test case for a test suite, keying off of the test case id.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - test_case_id: str. An id identifying the test case that you'd like to delete
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.test_suites.delete_test_suite_test_case(
            id="id",
            test_case_id="test_case_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", f"v1/test-suites/{id}/test-cases/{test_case_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTestSuitesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upsert_test_suite_test_case(
        self,
        id: str,
        *,
        upsert_test_suite_test_case_request_id: typing.Optional[str] = OMIT,
        label: typing.Optional[str] = OMIT,
        input_values: typing.List[NamedTestCaseVariableValueRequest],
        evaluation_values: typing.List[NamedTestCaseVariableValueRequest],
    ) -> TestSuiteTestCase:
        """
        Upserts a new test case for a test suite, keying off of the optionally provided test case id.

        If an id is provided and has a match, the test case will be updated. If no id is provided or no match
        is found, a new test case will be appended to the end.

        Note that a full replacement of the test case is performed, so any fields not provided will be removed
        or overwritten with default values.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - upsert_test_suite_test_case_request_id: typing.Optional[str].

            - label: typing.Optional[str].

            - input_values: typing.List[NamedTestCaseVariableValueRequest].

            - evaluation_values: typing.List[NamedTestCaseVariableValueRequest].
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suites.upsert_test_suite_test_case(
            id="id",
            input_values=[],
            evaluation_values=[],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"input_values": input_values, "evaluation_values": evaluation_values}
        if upsert_test_suite_test_case_request_id is not OMIT:
            _request["id"] = upsert_test_suite_test_case_request_id
        if label is not OMIT:
            _request["label"] = label
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", f"v1/test-suites/{id}/test-cases"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TestSuiteTestCase, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_test_suite_test_case(self, id: str, test_case_id: str) -> None:
        """
        Deletes an existing test case for a test suite, keying off of the test case id.

        Parameters:
            - id: str. A UUID string identifying this test suite.

            - test_case_id: str. An id identifying the test case that you'd like to delete
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.test_suites.delete_test_suite_test_case(
            id="id",
            test_case_id="test_case_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", f"v1/test-suites/{id}/test-cases/{test_case_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
