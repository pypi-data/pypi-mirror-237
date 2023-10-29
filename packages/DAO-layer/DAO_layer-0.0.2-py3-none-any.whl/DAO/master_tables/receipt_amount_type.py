from sqlalchemy import Column, Integer, String, Boolean
from DAO.base import BaseModel
from DAO.database import db


class ReceiptAmountTypeMaster(db.Model, BaseModel):
    __tablename__ = 'ReceiptAmountTypeMaster'

    ReceiptAmountType = Column(String(30), nullable=False)
    AccountMasterId = Column(Integer)
    AccountingChargeTypeMasterId = Column(Integer)
    IsActive = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.ReceiptAmountType}"
