from fastapi.exceptions import HTTPException
from sqlalchemy.sql.expression import desc
import models, schemas
import database
from fastapi import FastAPI, Depends, status
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
    # .order_by(models.Notes.date.desc)
    notes = db.query(models.Notes).all()
    return notes

@app.get("/notes/{id}")
def getNote(id, db:Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id==id).first()
    return note

@app.post("/notes")
def addNotes(request:schemas.NotesSchema, db: Session = Depends(get_db)):
    note = models.Notes(title=request.title, body=request.body)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

@app.put("/notes/{id}")
def updateNote(id, request:schemas.NotesSchema, db:Session = Depends(get_db)):
    updated_note = db.query(models.Notes).filter(models.Notes.id==id).first()
    if updated_note == None:
        HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} does not exist"
        )
    else:
        db.merge(updated_note)
        db.commit()
    return updated_note

@app.delete("/notes/{id}")
def deleteNotes(id, db:Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id==id).first()
    db.delete(note)
    db.commit()
    return note
