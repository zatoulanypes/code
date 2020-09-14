import re
import csv
import json
import requests
import pymorphy2

from bs4 import BeautifulSoup
from collections import Counter


def preprocess(text):
    '''
    Удаляет пунктуацию и приводит к нижнему регистру.
    :param text: исходный текст, str
    :return: список словоформ исходного текста, lst
    '''

    # удаляем пунктуацию (кроме тире, см. ниже) и прочие лишние символы, меняем регистр
    text = re.sub(r'[.,!?\\*«»():;"“”/+=…\s]', ' ', text).lower()

    # делим на словоформы, пробегаем по списку и удаляем тире
    word_list = list()
    for wf in text.split():
        if (wf.startswith('-')
                or wf.startswith('—')
                or wf.startswith('–')
                or wf.startswith('--')):
            continue
        else:
            word_list.append(wf)

    # На этапе предварительной обработки не удаляются тире, так как вместе с ними удалялись бы
    # и дефисы, которые не являются пунктуационными знаками. Тире убираются уже после разделения
    # текста на словоформы, когда они представляют собой отдельные вхождения в список или когда
    # с них начинаются другие вхождения (если тире не было отделено пробелом от следующего слова).

    return word_list


def build_freq(word_list, file_name):
    '''
    Строит частотный словарь и записывает его в файл CSV или JSON.
    :param word_list: список словоформ, lst
    :param file_name: имя файла для записи, str
    :return: None
    '''
    if file_name.endswith('.csv'):
        with open(file_name, 'w') as output:
            c = Counter()
            c.update(word_list)
            writer = csv.writer(output)
            for el in c.most_common():
                writer.writerow(el)

    elif file_name.endswith('.json'):
        with open(file_name, 'w') as output:
            c = Counter()
            c.update(word_list)
            json.dump(c.most_common(), output, indent=4, ensure_ascii=False)

    else:
        raise ValueError('CSV and JSON files only.')


def lemmatize(text):
    '''
    Для каждой словоформы в тексте находит ее лемму.
    :param text: исходный текст, str
    :return: список лемм, lst
    '''
    morph = pymorphy2.MorphAnalyzer()
    return [morph.parse(wf)[0].normal_form for wf in preprocess(text)]


def find_char_rep(char, n, word_list, file_name):
    '''
    Выбирает из списка слов те слова, в которых содержится ровно n
    символов char, и записывает их множество в файл txt.
    :param char: символ для поиска, str
    :param n: число повторений символа, int
    :param word_list: список слов для поиска, lst
    :param file_name: имя файла для записи, str
    :return: None
    '''
    s = set()

    for word in word_list:
        c = Counter()
        c.update(word)
        if c.get(char) == n:
            s.add(word)

    with open(file_name, 'w') as output:
        output.write('\n'.join(list(s)))


def main():
    with open('dom.txt', 'r') as input:
        text = input.read()

        # Часть 1
        build_freq(preprocess(text), 'freq1.csv')

        # Часть 2.1
        find_char_rep('о', 2, lemmatize(text), '2o.txt')

    # Часть 2.2
    r = requests.post('http://lib.ru/POEZIQ/PESSOA/lirika.txt')
    text = BeautifulSoup(r.content, features='html.parser').text
    build_freq(lemmatize(text), 'freq2.json')



if __name__ == '__main__':
    main()
