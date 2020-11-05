import re
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


def news_parser(link):
    pattern = re.compile(r'(?i).*(коронавирус|COVID-19).*')

    req = requests.get(link)
    soup = bs(req.content, features='html.parser')

    headers = soup.findAll('h3', attrs={'class': 'article_name'})
    clean_headers = [header.text for header in headers]
    covid_headers = [header for header in clean_headers if pattern.match(header) is not None]
    return covid_headers


def main():
    link = 'https://www.kommersant.ru/archive/rubric/4/month/2020-10-01'
    pprint(news_parser(link))


if __name__ == '__main__':
    main()