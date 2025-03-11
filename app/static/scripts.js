async function fetchNews() {
    let response = await fetch("/news");
    let news = await response.json();
    let list = document.getElementById("news-list");
    let detail = document.getElementById("news-detail");

    list.innerHTML = "";
    detail.innerHTML = "<p><<< Select News</p>";

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
    let detail = document.getElementById("news-detail");
    detail.innerHTML = `<iframe src="${link}" width="100%" height="600px" style="border:none;"></iframe>`;
}

fetchNews();