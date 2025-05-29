# lib/models/account_product.py
from sqlalchemy import Column, Integer, DateTime, ForeignKey, PrimaryKeyConstraint,func
from lib.models import Base
from sqlalchemy import Table
# tells SQLAlchemy that this table is part of the ORM's metadata and should be created in the database by use of base... and also has a timestamp
account_product = Table(
    "account_product",
    Base.metadata,
    Column("account_id", Integer, ForeignKey("account.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
    Column("start_date", DateTime),
    Column("end_date", DateTime),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, default=func.now(), onupdate=func.now())
)
