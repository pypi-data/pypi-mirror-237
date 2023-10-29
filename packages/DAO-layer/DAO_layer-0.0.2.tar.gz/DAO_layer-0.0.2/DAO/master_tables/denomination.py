from sqlalchemy import Column, Integer, String, Boolean
from DAO.base import BaseModel
from DAO.database import db


class DenominationMaster(db.Model, BaseModel):
    __tablename__ = 'DenominationMaster'

    DenominationValue = Column(Integer, nullable=False)
    DisplayName = Column(String(20), nullable=False)
    IsActive = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.DisplayName}"
