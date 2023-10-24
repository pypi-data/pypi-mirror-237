# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .document_document_to_document_index import DocumentDocumentToDocumentIndex
from .document_status import DocumentStatus
from .processing_state_enum import ProcessingStateEnum

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DocumentRead(pydantic.BaseModel):
    id: str
    external_id: typing.Optional[str] = pydantic.Field(
        description="The unique id of this document as it exists in the user's system."
    )
    last_uploaded_at: dt.datetime
    label: str = pydantic.Field(
        description="A human-readable label for the document. Defaults to the originally uploaded file's file name."
    )
    processing_state: typing.Optional[ProcessingStateEnum] = pydantic.Field(
        description=(
            "The current processing state of the document\n"
            "\n"
            "* `QUEUED` - Queued\n"
            "* `PROCESSING` - Processing\n"
            "* `PROCESSED` - Processed\n"
            "* `FAILED` - Failed\n"
        )
    )
    status: typing.Optional[DocumentStatus] = pydantic.Field(
        description=("The current status of the document\n" "\n" "* `ACTIVE` - Active\n")
    )
    original_file_url: typing.Optional[str]
    processed_file_url: typing.Optional[str]
    document_to_document_indexes: typing.List[DocumentDocumentToDocumentIndex]
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="A previously supplied JSON object containing metadata that can be filtered on when searching."
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
