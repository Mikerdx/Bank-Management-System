# lib/models/user_profile.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from lib.models import Base

class UserProfile(Base):
#map model to tablein database 
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

# Reverse one-to-one relationship
    account = relationship("Account", back_populates="profile", uselist=False)
