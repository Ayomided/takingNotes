from sqlalchemy import String, Column, Integer
from sqlalchemy.types import Date
from ..database import Base

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    title = Column(String)
    body = Column(String)
