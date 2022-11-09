import datetime

from sqlmodel import SQLModel, Field


class City(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    country_id: int = Field(default=None, foreign_key="country.id", nullable=False)
    name: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
