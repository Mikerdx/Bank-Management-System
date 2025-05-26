# lib/models/user_profile.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from lib.models import Base

class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(Text)

    # Reverse one-to-one relationship
    account = relationship("Account", back_populates="profile", uselist=False)
