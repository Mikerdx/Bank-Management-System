# lib/models/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.declarative import declared_attr

DATABASE_URL = "sqlite:///bank.db"
engine = create_engine(DATABASE_URL, echo=False, future=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
