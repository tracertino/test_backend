from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
# from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from users import Users
from sqlalchemy.orm import DeclarativeBase

# Base = declarative_base()
class Base(DeclarativeBase):
    pass

class Calculation(Base):
    __tablename__ = 'calculation'
    calc_id = Column(Integer,  ForeignKey(Users.id))
    fio = Column(String(200), nullable=False)
    birthday = Column(DateTime, nullable=False)
    calc = Column(String(200), nullable=True)
    # email = Column(String(50), nullable=False)
    # user_name = Column(String(20), nullable=False)
    # family_name = Column(String(20), nullable=False)
    # last_name = Column(String(20), nullable=True)
    # password = Column(String(50), nullable=False)
    # birthday = Column(DateTime, nullable=False) 
    # role = Column(String(10), nullable=False)
    # token =  Column(String(200), nullable=False) 
    