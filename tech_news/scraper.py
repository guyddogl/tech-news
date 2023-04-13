# Requisito 1
import time
import requests
from parsel import Selector


def fetch(url):
    time.sleep(1)
    try:
        result = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if result.status_code == 200:
            return result.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css(".entry-title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = (
        selector.css("div.entry-header-inner h1.entry-title::text")
        .get()
        .strip()
    )

    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get().split()[0]
    time = "".join(filter(str.isdigit, reading_time))
    summary = selector.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()
    summary = "".join(summary).strip()
    category = selector.css("div.meta-category a span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(time),
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
