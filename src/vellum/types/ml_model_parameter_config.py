# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .open_api_number_property import OpenApiNumberProperty
from .open_api_integer_property import OpenApiIntegerProperty
from .open_api_array_property import OpenApiArrayProperty
from .open_api_object_property import OpenApiObjectProperty
from .open_api_property import OpenApiProperty
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MlModelParameterConfig(UniversalBaseModel):
    temperature: typing.Optional[OpenApiNumberProperty] = None
    max_tokens: typing.Optional[OpenApiIntegerProperty] = None
    stop: typing.Optional[OpenApiArrayProperty] = None
    top_p: typing.Optional[OpenApiNumberProperty] = None
    top_k: typing.Optional[OpenApiIntegerProperty] = None
    frequency_penalty: typing.Optional[OpenApiNumberProperty] = None
    presence_penalty: typing.Optional[OpenApiNumberProperty] = None
    logit_bias: typing.Optional[OpenApiObjectProperty] = None
    custom_parameters: typing.Optional[typing.Dict[str, typing.Optional[OpenApiProperty]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
