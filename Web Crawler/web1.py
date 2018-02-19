import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.flipkart.com/search?q=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a'):
            href = link.get('href')
            print(href)
        page += 1
trade_spider(1)
