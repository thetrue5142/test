import os, sys
from alembic import context
from dotenv import load_dotenv
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
sys.path.append(app_dir)
from urllib.parse import urlparse
from database import Base, async_engine
import models

config = context.config
load_dotenv()
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
config.set_main_option("sqlalchemy.url", f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require")
target_metadata = Base.metadata

def run_migrations_online():
    connectable = async_engine

    async def do_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(lambda conn: context.configure(connection=conn, target_metadata=target_metadata))
            await connection.run_sync(lambda _: context.run_migrations())

    import asyncio
    asyncio.run(do_migrations())

run_migrations_online()