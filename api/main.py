from fastapi import FastAPI
from sqlalchemy.orm import Session
from .models import models

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/notes")
def getNotes():
    return {"Hey": "Hey"}