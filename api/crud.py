from sqlalchemy.orm import Session

from .models import models
from . import schemas

def getNotes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notes).offset(skip).limit(limit).all()

def addNotes(db: Session, note: schemas.NotesCreate, id: int):
    note = models.Notes(**note.dict(), id=id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
