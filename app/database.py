# Database

import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from urllib.parse import urlparse

load_dotenv()
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
async_engine = create_async_engine(f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require", echo=True)
SessionLocal = async_sessionmaker(bind=async_engine, class_=AsyncSession)