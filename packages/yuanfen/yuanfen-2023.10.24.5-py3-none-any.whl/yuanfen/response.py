from pydantic import BaseModel
from typing import Optional, Any


class BaseResponse(BaseModel):
    code: int
    message: str
    data: Optional[Any]

    def dict(self, *args, **kwargs) -> dict[str, Any]:
        """
        Override the default dict method to exclude None values in the response
        """
        kwargs.pop("exclude_none", None)
        return super().dict(*args, exclude_none=True, **kwargs)


class SuccessResponse(BaseResponse):
    code: int = 0
    message: str = "SUCCESS"


class ErrorResponse(BaseResponse):
    code: int = 1000
    message: str = "ERROR"
