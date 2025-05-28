# lib/models/transaction.py
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime,func
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.models import Base

class Transaction(Base):
    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    type = Column(String)  # 'deposit' or 'withdrawal'
    amount = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    account = relationship("Account", back_populates="transactions")
