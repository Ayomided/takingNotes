from sqlalchemy import String, Column, Integer
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.types import Date
from datetime import datetime
import database

class Notes(database.Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.now)
    title = Column(String)
    body = Column(String)
