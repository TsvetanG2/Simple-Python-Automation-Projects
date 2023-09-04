import requests
from bs4 import BeautifulSoup


def get_web_page(domain):
    response = requests.get(domain)

    soup = BeautifulSoup(response.content, 'html.parser')
    js_tag = input('Enter the Javascript tag you are looking for: ')
    javascript = soup.find(js_tag)
    print(javascript)

    with open("scrapedJavaScript.txt", 'w', encoding="utf-8") as f:
        f.write(str(soup.find_all))


get_web_page(input('Which domain would you like to scrape? '))
