async function fetchNews() {
    let response = await fetch("/news");
    let news = await response.json();
    let list = document.getElementById("news-list");
    list.innerHTML = news.map(n => `<li><a href="${n.link}" target="_blank">${n.title}</a></li>`).join("");
}
fetchNews();