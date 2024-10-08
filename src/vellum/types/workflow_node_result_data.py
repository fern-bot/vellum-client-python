# This file was auto-generated by Fern from our API Definition.

import typing
from .prompt_node_result import PromptNodeResult
from .search_node_result import SearchNodeResult
from .templating_node_result import TemplatingNodeResult
from .code_execution_node_result import CodeExecutionNodeResult
from .conditional_node_result import ConditionalNodeResult
from .api_node_result import ApiNodeResult
from .terminal_node_result import TerminalNodeResult
from .merge_node_result import MergeNodeResult
from .subworkflow_node_result import SubworkflowNodeResult
from .metric_node_result import MetricNodeResult
from .map_node_result import MapNodeResult

WorkflowNodeResultData = typing.Union[
    PromptNodeResult,
    SearchNodeResult,
    TemplatingNodeResult,
    CodeExecutionNodeResult,
    ConditionalNodeResult,
    ApiNodeResult,
    TerminalNodeResult,
    MergeNodeResult,
    SubworkflowNodeResult,
    MetricNodeResult,
    MapNodeResult,
]
