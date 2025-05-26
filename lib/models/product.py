# lib/models/product.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from lib.models import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)

    accounts = relationship(
        "Account",
        secondary="account_product",
        back_populates="products"
    )
