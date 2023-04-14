from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    categories = []

    for news in find_news():
        categories.append(news["category"])

    count = Counter(sorted(categories))

    return sorted(count, key=count.get, reverse=True)[0:5]
