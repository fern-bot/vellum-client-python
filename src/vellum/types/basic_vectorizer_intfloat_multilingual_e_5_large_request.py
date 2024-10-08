# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BasicVectorizerIntfloatMultilingualE5LargeRequest(UniversalBaseModel):
    """
    Basic vectorizer for intfloat/multilingual-e5-large.
    """

    config: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    model_name: typing.Literal["intfloat/multilingual-e5-large"] = "intfloat/multilingual-e5-large"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
