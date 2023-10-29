from sqlalchemy import Column, String, Boolean
from DAO.base import BaseModel
from DAO.database import db


class TransferTypeMaster(db.Model, BaseModel):
    __tablename__ = 'TransferTypeMaster'

    TransferType = Column(String(30), nullable=False)
    IsActive = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.TransferType}"
