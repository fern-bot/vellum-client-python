# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .ml_model_display_tag_enum_value_label import MlModelDisplayTagEnumValueLabel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class MlModelDisplayConfigLabelled(UniversalBaseModel):
    label: str
    description: str
    tags: typing.List[MlModelDisplayTagEnumValueLabel]
    default_display_priority: typing.Optional[float] = pydantic.Field(default=None)
    """
    Can only be set when using an internal service token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
