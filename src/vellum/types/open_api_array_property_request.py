# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class OpenApiArrayPropertyRequest(UniversalBaseModel):
    """
    An OpenAPI specification of a property with type 'array'
    """

    type: typing.Literal["array"] = "array"
    min_items: typing.Optional[int] = None
    max_items: typing.Optional[int] = None
    unique_items: typing.Optional[bool] = None
    items: "OpenApiPropertyRequest"
    prefix_items: typing.Optional[typing.List["OpenApiPropertyRequest"]] = None
    contains: typing.Optional["OpenApiPropertyRequest"] = None
    min_contains: typing.Optional[int] = None
    max_contains: typing.Optional[int] = None
    default: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .open_api_property_request import OpenApiPropertyRequest  # noqa: E402

update_forward_refs(OpenApiArrayPropertyRequest)
