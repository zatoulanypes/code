import json
import requests
from bs4 import BeautifulSoup


def collect_corpus():
    corpus = []

    page = 0
    link = 'https://knife.media/category/news/page/'
    date = ''

    while not date.endswith('октября 2019'):
        page += 1
        page_req = requests.get(link + str(page))
        if page_req.status_code == 200:
            page_soup = BeautifulSoup(page_req.content, features='html.parser')
            articles = page_soup.findAll('div', class_='widget-news__wrapper')

            for article in articles:
                art_link = article.findAll('a', class_='widget-news__content-link')[0]['href']
                art_date = article.find('time').text
                art_tags = [tag.text for tag in article.findAll('a', class_='meta__item')]

                art_req = requests.get(art_link)
                if art_req.status_code == 200:
                    art_soup = BeautifulSoup(art_req.content, features='html.parser')

                    art_title = art_soup.find('h1').text
                    art_entry = art_soup.findAll('div', class_='entry-content')[0]
                    art_text = '\n'.join([p.text for p in art_entry.findAll(['h1', 'p', 'h4'], recursive=False)])

                    data = {
                        'Title': art_title,
                        'Date': art_date,
                        'Tags': art_tags,
                        'Link': art_link,
                        'Text': art_text
                    }
                    corpus.append(data)
                    print(art_date)

                date = art_date

    return corpus


def main():
    corpus = collect_corpus()
    with open('knife_corpus.json', 'w', encoding='utf-8') as file:
        json.dump(corpus, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()