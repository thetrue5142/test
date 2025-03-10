# FastAPI

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models import News
from app.scrape import fetch_udn_news
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    async def background_update():
        while True:
            await fetch_udn_news()

    task = asyncio.create_task(background_update())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

app.mount("/static/templates", StaticFiles(directory="../app/templates"), name="static_templates")
app.mount("/static", StaticFiles(directory="../app/static"), name="static")

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

@app.get("/news")
async def get_news(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(News))
    news_list = result.scalars().all()
    return [{"title": news.title, "link": news.link} for news in news_list]

@app.get("/")
async def serve_index():
    return FileResponse("../app/templates/index.html")