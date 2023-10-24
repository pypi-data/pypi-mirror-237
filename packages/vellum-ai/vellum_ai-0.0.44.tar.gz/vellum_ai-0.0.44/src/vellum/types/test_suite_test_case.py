# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .evaluation_params import EvaluationParams

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TestSuiteTestCase(pydantic.BaseModel):
    test_case_id: typing.Optional[str] = pydantic.Field(
        description="The id of the test case to update. If none is provided, an id will be generated and a new test case will be appended."
    )
    label: typing.Optional[str] = pydantic.Field(description="A human-friendly label for the test case.")
    input_values: typing.Dict[str, typing.Any] = pydantic.Field(
        description="Key/value pairs for each input variable that the Test Suite expects."
    )
    evaluation_params: EvaluationParams = pydantic.Field(
        description="Parameters to use when evaluating the test case, specific to the test suite's evaluation metric."
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
