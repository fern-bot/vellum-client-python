# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .scenario_input import ScenarioInput
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SandboxScenario(UniversalBaseModel):
    """
    Sandbox Scenario
    """

    label: typing.Optional[str] = None
    inputs: typing.List[ScenarioInput] = pydantic.Field()
    """
    The inputs for the scenario
    """

    id: str = pydantic.Field()
    """
    The id of the scenario
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
