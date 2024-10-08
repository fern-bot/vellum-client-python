# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WorkflowOutputJson(UniversalBaseModel):
    """
    A JSON output from a Workflow execution.
    """

    id: str
    name: str = pydantic.Field()
    """
    The output's name, as defined in the workflow
    """

    type: typing.Literal["JSON"] = "JSON"
    value: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
