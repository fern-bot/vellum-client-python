# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
import typing
from .open_api_integer_property_request import OpenApiIntegerPropertyRequest
from .open_api_number_property_request import OpenApiNumberPropertyRequest
from .open_api_string_property_request import OpenApiStringPropertyRequest
from .open_api_boolean_property_request import OpenApiBooleanPropertyRequest
from .open_api_const_property_request import OpenApiConstPropertyRequest
from .open_api_ref_property_request import OpenApiRefPropertyRequest
import typing

if typing.TYPE_CHECKING:
    from .open_api_array_property_request import OpenApiArrayPropertyRequest
    from .open_api_object_property_request import OpenApiObjectPropertyRequest
    from .open_api_one_of_property_request import OpenApiOneOfPropertyRequest
OpenApiPropertyRequest = typing.Union[
    "OpenApiArrayPropertyRequest",
    "OpenApiObjectPropertyRequest",
    OpenApiIntegerPropertyRequest,
    OpenApiNumberPropertyRequest,
    OpenApiStringPropertyRequest,
    OpenApiBooleanPropertyRequest,
    "OpenApiOneOfPropertyRequest",
    OpenApiConstPropertyRequest,
    OpenApiRefPropertyRequest,
]
