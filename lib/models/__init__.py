# lib/models/__init__.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Tells SQLAlchemy to use an SQLite database file named bank.db in your project directory.
DATABASE_URL = "sqlite:///bank.db"

#Connection maker (creates a database engine ) and generate database sessions
engine = create_engine(DATABASE_URL, echo=False, future=True)
Session = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

# Ensure models are imported so they're registered before metadata creation
from . import account
from . import transaction
from . import user_profile
from . import bank_branch
from . import product
from . import account_product

#drops all tables and create them from scratch
def reset_database():
    """Drop all tables and recreate them — use only during development."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

#initialise database
def init_database():
    """Create tables if they don't exist."""
    Base.metadata.create_all(engine)
