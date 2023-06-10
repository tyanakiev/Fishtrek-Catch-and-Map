from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    fish = relationship("Fish", back_populates="owner")


class Fish(Base):
    __tablename__ = "fish"

    id = Column(Integer, primary_key=True, index=True)
    species = Column(String)
    length = Column(Float)
    weight = Column(Float)
    is_released = Column(Boolean)
    catch_date = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="fish")
