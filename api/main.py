import models, schemas
import database
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

models.database.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def root():
    return {"Hey": "Hey"}

@app.get("/notes")
def getNotes(db:Session = Depends(get_db)):
    notes = db.query(models.Notes).all()
    return notes

@app.post("/notes")
def addNotes(request:schemas.NotesSchema, db: Session = Depends(get_db)):
    note = models.Notes(title=request.title, body=request.body)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

@app.delete("/notes/{id}")
def deleteNotes(id, db:Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id==id).first()
    db.delete(note)
    db.commit()
    return note
