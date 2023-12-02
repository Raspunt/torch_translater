from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from src.db.db_base import Base


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    level = Column(String)
    message = Column(String)
