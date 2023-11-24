from pydantic import BaseModel


class ForecastRequest(BaseModel):
    text: str


class ForecastResponse(BaseModel):
    group: str
    sub: str
    location: str
    department: str
    text: str
