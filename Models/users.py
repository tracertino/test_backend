from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, autoincrement="auto")
    # email = Column(String(50), nullable=False)
    user_name = Column(String(20), nullable=False)
    family_name = Column(String(20), nullable=False)
    # last_name = Column(String(20), nullable=True)
    # password = Column(String(30), nullable=False)
    # birthday = Column(DateTime, nullable=False) 
    # role = Column(String(10), nullable=False)
    # token =  Column(String(200), nullable=False) 
    # calculation = relationship("Calculation")
    