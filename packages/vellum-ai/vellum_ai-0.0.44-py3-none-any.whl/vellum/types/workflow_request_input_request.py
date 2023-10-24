# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .workflow_request_chat_history_input_request import WorkflowRequestChatHistoryInputRequest
from .workflow_request_json_input_request import WorkflowRequestJsonInputRequest
from .workflow_request_string_input_request import WorkflowRequestStringInputRequest


class WorkflowRequestInputRequest_String(WorkflowRequestStringInputRequest):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowRequestInputRequest_Json(WorkflowRequestJsonInputRequest):
    type: typing_extensions.Literal["JSON"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class WorkflowRequestInputRequest_ChatHistory(WorkflowRequestChatHistoryInputRequest):
    type: typing_extensions.Literal["CHAT_HISTORY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


WorkflowRequestInputRequest = typing.Union[
    WorkflowRequestInputRequest_String, WorkflowRequestInputRequest_Json, WorkflowRequestInputRequest_ChatHistory
]
