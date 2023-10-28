from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from DAO.base import BaseModel
from DAO.database import db

class DenominationMaster(db.Model, BaseModel):
    __tablename__ = 'DenominationMaster'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    DenominationValue = Column(Integer, nullable=False)
    DisplayName = Column(String(20), nullable=False)
    IsActive = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"{self.DisplayName}"
