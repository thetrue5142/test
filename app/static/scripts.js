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
    let response = await fetch(link);
    let text = await response.text();
    
    let detail = document.getElementById("news-detail");
    detail.innerHTML = "<p>新聞內容正在載入...</p>";
    detail.innerHTML = text;
}

fetchNews();