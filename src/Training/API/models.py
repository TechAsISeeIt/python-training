from pydantic import BaseModel


class StudentResponse(BaseModel):
    ID: int
    NAME: str
    SCORE: int


class Students(BaseModel):
    items: list[StudentResponse]
