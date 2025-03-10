import os, sys
from alembic import context
from dotenv import load_dotenv
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.dirname(current_dir)
sys.path.append(app_dir)
from models import News
from urllib.parse import urlparse

config = context.config
load_dotenv()
tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
config.set_main_option("sqlalchemy.url", f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require")
target_metadata = News.metadata