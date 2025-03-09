import requests
from bs4 import BeautifulSoup
from database import SessionLocal, News
import asyncio
from sqlalchemy import text

url = "https://tw-nba.udn.com/nba/index"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    
    news_list_body = soup.select_one("div#news_list_body")
    
    if news_list_body:
        for item in news_list_body.select("a"):
            title = item.text.strip()
            link = item["href"]
            if not link.startswith("http"):
                link = "https://udn.com" + link
            articles.append({"title": title, "link": link})
        
        if articles:
            print("Get articles ：")
            for article in articles:
                print(f"title: {article['title']}, link: {article['link']}")
            
            async def save_news(articles):
                try:
                    async with SessionLocal() as session:
                        result = await session.execute(text("SELECT 1"))
                        print("connected to database")
                        
                        for article in articles:
                            news = News(title=article["title"], link=article["link"])
                            session.add(news)
                        
                        await session.commit()
                        print("saved to database")
                except Exception as e:
                    print(f"database error: {e}")

            asyncio.run(save_news(articles))

        else:
            print("Didn't find any news")
    else:
        print("Please correct id selector")
else:
    print(f"Fail:{response.status_code}")