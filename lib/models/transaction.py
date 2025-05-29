# lib/models/transaction.py
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime,func
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.models import Base

class Transaction(Base):
#Maps this model to the transaction table in the database.
    __tablename__ = 'transaction'
#Column addition 
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    type = Column(String)  # 'deposit' or 'withdrawal'
    amount = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

#R/ship
    account = relationship("Account", back_populates="transactions")
