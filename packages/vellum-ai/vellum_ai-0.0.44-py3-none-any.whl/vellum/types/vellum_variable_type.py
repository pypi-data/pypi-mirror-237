# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VellumVariableType(str, enum.Enum):
    """
    * `STRING` - STRING
    * `NUMBER` - NUMBER
    * `JSON` - JSON
    * `CHAT_HISTORY` - CHAT_HISTORY
    * `SEARCH_RESULTS` - SEARCH_RESULTS
    * `ERROR` - ERROR
    """

    STRING = "STRING"
    NUMBER = "NUMBER"
    JSON = "JSON"
    CHAT_HISTORY = "CHAT_HISTORY"
    SEARCH_RESULTS = "SEARCH_RESULTS"
    ERROR = "ERROR"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        chat_history: typing.Callable[[], T_Result],
        search_results: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VellumVariableType.STRING:
            return string()
        if self is VellumVariableType.NUMBER:
            return number()
        if self is VellumVariableType.JSON:
            return json()
        if self is VellumVariableType.CHAT_HISTORY:
            return chat_history()
        if self is VellumVariableType.SEARCH_RESULTS:
            return search_results()
        if self is VellumVariableType.ERROR:
            return error()
