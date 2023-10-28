from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from DAO.base import BaseModel
from DAO.database import db

class TransferTypeMaster(db.Model, BaseModel):
    __tablename__ = 'TransferTypeMaster'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    TransferType = Column(String(30), nullable=False)
    IsActive = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.TransferType}"

