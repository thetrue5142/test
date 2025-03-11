async function fetchNews() {
    let response = await fetch("/news");
    let news = await response.json();
    let list = document.getElementById("news-list");
    let detail = document.getElementById("news-detail");

    list.innerHTML = "";
    detail.innerHTML = "<p>Work in Progress...</p>";

    news.forEach(n => {
        let newsItem = document.createElement("a");
        newsItem.href = "#";
        newsItem.textContent = n.title;
        newsItem.onclick = function () {
            event.preventDefault();
            showNewsDetail(n.link);
        };
        list.appendChild(newsItem);
    });
}

async function showNewsDetail(link) {
    let response = await fetch(`/get_news_detail?link=${encodeURIComponent(link)}`);
    let data = await response.json();
    
    let detail = document.getElementById("news-detail");
    if (data.content) {
        detail.innerHTML = data.content;
    } else {
        detail.innerHTML = "<p>error</p>";
    }
}


fetchNews();