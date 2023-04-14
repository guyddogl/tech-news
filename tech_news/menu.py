from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories
import sys


def option_0():
    amount_news = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(amount_news)


def option_1():
    by_title = input("Digite o título:")
    return search_by_title(by_title)


def option_2():
    by_date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(by_date)


def option_3():
    by_category = input("Digite a categoria:")
    return search_by_category(by_category)


# Requisitos 11 e 12
def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
 """
    )
    if any(option == str(i) for i in range(4)):
        eval(f"option_{option}")()
    elif option == "4":
        return top_5_categories()
    elif option == "5":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)
