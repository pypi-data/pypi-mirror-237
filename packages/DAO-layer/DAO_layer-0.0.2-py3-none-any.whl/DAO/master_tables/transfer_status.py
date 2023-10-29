from sqlalchemy import Column, String, Boolean
from DAO.base import BaseModel
from DAO.database import db


class TransferStatusMaster(db.Model, BaseModel):
    __tablename__ = 'TransferStatusMaster'

    StatusName = Column(String(30), nullable=False)
    IsActive = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.StatusName}"
