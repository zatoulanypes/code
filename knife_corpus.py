import json
import requests
from bs4 import BeautifulSoup


def parse_article(article):
    url = article.findAll('a', class_='widget-news__content-link')[0]['href']
    req = requests.get(url)

    if req.status_code == 200:
        soup = BeautifulSoup(req.content, features='html.parser')

        title = soup.find('h1').text
        author = soup.findAll('a', attrs={'rel': 'author'})[0].text
        date = soup.find('time').text
        tags = [tag.text for tag in soup.findAll('a', attrs={'rel': 'tag'})]
        entry = soup.findAll('div', class_='entry-content')[0]
        text = '\n'.join([p.text for p in entry.findAll(['h1', 'p', 'h4'], recursive=False)])

        return {
            'Title': title,
            'Author': author,
            'Date': date,
            'Tags': tags,
            'Link': url,
            'Text': text
        }


def parse_page(page, url=None):
    url = url or 'https://knife.media/category/news/page/'
    req = requests.get(url + str(page))

    if req.status_code == 200:
        soup = BeautifulSoup(req.content, features='html.parser')
        articles = soup.findAll('div', class_='widget-news__wrapper')

        return [parse_article(article) for article in articles]


def collect_corpus():
    corpus = []
    page = 0
    date = ''

    while not date.endswith('октября 2019'):
        page += 1
        corpus.extend(parse_page(page))
        date = corpus[-1]['Date']
        print(date)

    return corpus


def main():
    corpus = collect_corpus()
    with open('knife_corpus.json', 'w', encoding='utf-8') as file:
        json.dump(corpus, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
