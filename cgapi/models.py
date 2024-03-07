from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Player(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    points: int
    date: datetime = Field(datetime.now())
