# models
from sqlalchemy import Column, Integer, String, Text, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(Text)
    content = Column(Text)
    published_at = Column(DateTime, server_default=func.now())
