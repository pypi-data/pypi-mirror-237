from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from DAO_layer.base import BaseModel
from DAO.database import db
from requests.status_codes import codes

class AccountingChargeTypeMaster(db.Model, BaseModel):
    __tablename__ = 'AccountingChargeTypeMaster'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    AccountingChargeType = Column(String(30), nullable=False)
    IsActive = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"{self.AccountingChargeType}"
