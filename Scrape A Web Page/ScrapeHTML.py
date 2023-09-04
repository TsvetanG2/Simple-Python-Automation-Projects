import requests
from bs4 import BeautifulSoup


def get_web_page(domain):
    response = requests.get(domain)

    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.find_all())

    with open("scrapedWebHTML.txt", 'w', encoding="utf-8") as f:
        f.write(str(soup.find_all))


get_web_page(input('Which domain would you like to scrape? '))

