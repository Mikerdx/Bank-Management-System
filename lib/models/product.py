# lib/models/product.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from lib.models import Base

class Product(Base):
#Map this model to the product table in  database.tells the name of table as in database
    __tablename__ = 'product'
#column creation and timestamp addition
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

#R/ship (many to many)
    accounts = relationship(
        "Account",
        secondary="account_product",
        back_populates="products"
    )
