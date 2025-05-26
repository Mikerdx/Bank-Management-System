# lib/models/bank_branch.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base

class BankBranch(Base):
    __tablename__ = 'bank_branch'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    accounts = relationship("Account", back_populates="branch")
