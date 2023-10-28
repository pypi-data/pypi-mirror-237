from abc import ABC

from pydantic import BaseModel


class RequiresOperationName(ABC, BaseModel):
    """Requires an operation name."""

    operation_name: str


class RequiresBody(ABC, BaseModel):
    """Requires a request body."""

    body: BaseModel
