# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .open_ai_vectorizer_config_request import OpenAiVectorizerConfigRequest
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OpenAiVectorizerTextEmbedding3LargeRequest(UniversalBaseModel):
    """
    OpenAI vectorizer for text-embedding-3-large.
    """

    config: OpenAiVectorizerConfigRequest
    model_name: typing.Literal["text-embedding-3-large"] = "text-embedding-3-large"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
