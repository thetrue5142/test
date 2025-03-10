from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models import News
import asyncio
import time

async def fetch_udn_news():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://tw-nba.udn.com/nba/index")

    time.sleep(3)

    articles = []
    news_list_body = driver.find_elements(By.CSS_SELECTOR, "div#news_list_body a")

    for item in news_list_body:
        title = item.text.strip()
        link = item.get_attribute("href")
        if link:
            articles.append({"title": title, "link": link})

    driver.quit()
    
    if articles:
        await save_news_to_db(articles)

async def save_news_to_db(articles):
    async with SessionLocal() as session:
        try:
            existing_news = await session.execute(select(News.title))
            existing_titles = {row[0] for row in existing_news.all()}

            new_articles = [News(title=a["title"], link=a["link"]) for a in articles if a["title"] not in existing_titles]

            if new_articles:
                session.add_all(new_articles)
                await session.commit()
                print(f"Save {len(new_articles)} News to Database")
            else:
                print("No new news to save")
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    asyncio.run(fetch_udn_news())