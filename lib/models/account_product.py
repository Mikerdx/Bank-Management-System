# lib/models/account_product.py
from sqlalchemy import Column, Integer, DateTime, ForeignKey, PrimaryKeyConstraint
from lib.models import Base

class AccountProduct(Base):
    __tablename__ = 'account_product'

    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    __table_args__ = (
        PrimaryKeyConstraint('account_id', 'product_id'),
    )
