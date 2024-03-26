from datetime import date
from pydantic import BaseModel

class NotesBase(BaseModel):
    id: int
    date: date
    title: str
    body: str

    class Config:
        orm_mode = True