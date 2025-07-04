from pydantic import BaseModel, Field
from typing import Optional

class WeatherAlert(BaseModel):
    id: Optional[int] = None
    city: str
    condition: str
    threshold: float
    email: str
    active: bool = True
