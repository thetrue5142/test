# Database

import os
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

sync_engine = create_engine(f"postgresql://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}")

async_engine = create_async_engine(
    f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require", 
    echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=False)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def async_main() -> None:
    async with async_engine.connect() as conn:
        result = await conn.execute(text("select 'hello world'"))
        print(result.fetchall())
    await async_engine.dispose()

async def init_and_query():
    await init_db()
    await async_main()

if __name__ == "__main__":
    asyncio.run(init_and_query())