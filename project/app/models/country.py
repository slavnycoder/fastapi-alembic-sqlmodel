from sqlmodel import SQLModel, Field


class Country(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
