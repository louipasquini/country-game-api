from datetime import datetime

from pydantic import BaseModel


class PlayerOut(BaseModel):
    id: int
    name: str
    points: int
    date: datetime


class PlayerIn(BaseModel):
    name: str
    points: int
