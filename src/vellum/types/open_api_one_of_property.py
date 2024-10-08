# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class OpenApiOneOfProperty(UniversalBaseModel):
    """
    An OpenAPI specification of a property with type 'oneOf'
    """

    type: typing.Literal["oneOf"] = "oneOf"
    one_of: typing.List["OpenApiProperty"] = pydantic.Field(alias="oneOf")
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .open_api_property import OpenApiProperty  # noqa: E402

update_forward_refs(OpenApiOneOfProperty)
