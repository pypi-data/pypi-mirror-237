from sqlalchemy import Column, String, Boolean
from DAO.base import BaseModel
from DAO.database import db


class PlatformMaster(db.Model, BaseModel):
    __tablename__ = 'PlatformMaster'

    PlatformName = Column(String(30), nullable=False)
    IsActive = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.PlatformName}"
