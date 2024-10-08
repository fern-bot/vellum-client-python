# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .search_result_document_request import SearchResultDocumentRequest
from .search_result_meta_request import SearchResultMetaRequest
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchResultRequest(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The text of the chunk that matched the search query.
    """

    score: float = pydantic.Field()
    """
    A score representing how well the chunk matches the search query.
    """

    keywords: typing.List[str]
    document: SearchResultDocumentRequest = pydantic.Field()
    """
    The document that contains the chunk that matched the search query.
    """

    meta: typing.Optional[SearchResultMetaRequest] = pydantic.Field(default=None)
    """
    Additional information about the search result.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
