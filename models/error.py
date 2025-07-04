from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str  # or title
    message: str  # or detail
    status_code: int
