# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .map_node_result_data import MapNodeResultData
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MapNodeResult(UniversalBaseModel):
    """
    A Node Result Event emitted from a Map Node.
    """

    type: typing.Literal["MAP"] = "MAP"
    data: typing.Optional[MapNodeResultData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
