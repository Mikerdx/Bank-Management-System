# lib/models/bank_branch.py
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from lib.models import Base

class BankBranch(Base):
#map the account model to the table in database
    __tablename__ = 'bank_branch'
#column creation
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
#R/ship of one to many
    accounts = relationship("Account", back_populates="branch")
