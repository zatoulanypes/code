import pymorphy2
import random
from itertools import islice, product
from pprint import pprint


def take(n, m, xs):
    res = list(islice(xs, 0, n))
    random.shuffle(res)
    return res[:m]


def lists(d, morph):
    adjfs = []
    nouns = []
    count = 0
    for line in d:
        if count == 1000:
            break
        else:
            token = line.strip()
            p = morph.parse(token)[0]
            if p.tag.POS == 'ADJF':
                count += 1
                adjfs.append(p.normalized)
            elif p.tag.POS == 'NOUN':
                count += 1
                nouns.append(p.normalized)
    return adjfs, nouns


def generator(adjfs, nouns):
    for pair in product(adjfs, nouns):
        try:
            yield pair[0].inflect({pair[1].tag.gender}).word + ' ' + pair[1].normal_form
        except ValueError:
            pass


with open('rus_shuffled.txt', 'r') as file:
    d = file.readlines()
    morph = pymorphy2.MorphAnalyzer()
    adjfs, nouns = lists(d, morph)

    pprint(take(10000, 50, generator(adjfs, nouns)))