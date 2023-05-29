import requests
from bs4 import BeautifulSoup as bs


#url1 = f"https://scholar.google.com/scholar?start=0&q={query}&hl=en&scisbd=1&as_sdt=0,5"


def get_article_blocks(query):
    url = f"https://scholar.google.com/scholar?start=0&q={query}&hl=en&scisbd=1&as_sdt=0,5"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    article_blocks = soup.find_all('div', {'class': 'gs_r gs_or gs_scl'})
    return article_blocks


def get_article_info(query):
    article_blocks = get_article_blocks(query)
    articles = []

    for article_block in article_blocks:
        if article_block.find('div', {'class': 'gs_ggs gs_fl'}):
            title = article_block.find('h3', {'class': 'gs_rt'}
                        ).text.replace('[PDF]', '').replace('[HTML]', '').strip()
            url = article_block.find('div', {'class': 'gs_or_ggsm'}).find('a')['href']
            articles.append((title, url))

    return articles