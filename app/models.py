# Models

from sqlalchemy import Column, Integer, String, Text
from .database import async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)
    content = Column(Text, nullable=True)
