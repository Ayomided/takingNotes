from datetime import date
from pydantic import BaseModel

class NotesSchema(BaseModel):
    id: int
    d: date = None
    title: str = None
    body: str = None

    # class Config:
    #     orm_mode = True
