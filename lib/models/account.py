# lib/models/account.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from lib.models import Base

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    user_pw = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    profile_id = Column(Integer, ForeignKey('user_profile.id'), unique=True)
    branch_id = Column(Integer, ForeignKey('bank_branch.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


    profile = relationship("UserProfile", back_populates="account", uselist=False)
    branch = relationship("BankBranch", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
    products = relationship(
        "Product",
        secondary="account_product",
        back_populates="accounts"
    )
