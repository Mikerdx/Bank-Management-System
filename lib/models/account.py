# lib/models/account.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from lib.models import Base
from lib.models.account_product import account_product

class Account(Base):
#map the account model to the table in database
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    user_pw = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    profile_id = Column(Integer, ForeignKey('user_profile.id'), unique=True)
    branch_id = Column(Integer, ForeignKey('bank_branch.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


#relationships
#one to one
    profile = relationship("UserProfile", back_populates="account", uselist=False)
#many to one
    branch = relationship("BankBranch", back_populates="accounts")
#one to many
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")
#many to many
    products = relationship(
    "Product",
    secondary=account_product,
    back_populates="accounts"
)

