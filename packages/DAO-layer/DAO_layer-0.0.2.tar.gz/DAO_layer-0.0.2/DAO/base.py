from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func


class IdEntityModel:
    Id = Column(Integer, primary_key=True, autoincrement=True)


class AuditEntityModel:
    Created = Column(DateTime, nullable=False, default=func.now())
    CreatedBy = Column(String(50), nullable=False)
    CreaterIp = Column(String(50), nullable=False)
    CreaterMac = Column(String(50), nullable=False)
    Modified = Column(DateTime, nullable=True, onupdate=func.now())
    ModifiedBy = Column(String(50), nullable=True)
    ModifierIp = Column(DateTime, nullable=True)
    ModifierMac = Column(String(50), nullable=True)


class BaseModel(IdEntityModel, AuditEntityModel):
    pass


class DeleteModel:
    Deleted = Column(DateTime)
    DeletedBy = Column(String(50))
