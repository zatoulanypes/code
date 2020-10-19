import pickle
from corus import load_corpora


class UnigramMorphAnalyzer:

    records = load_corpora('annot.opcorpora.xml.byfile.zip')
    endings_stat = dict()

    def __init__(self):
        self.endings_stat = UnigramMorphAnalyzer.endings_stat


    def __getitem__(self, key):
        return UnigramMorphAnalyzer.endings_stat[key]


    def train(self):

        for rec in UnigramMorphAnalyzer.records:
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        for i in [1, 2, 3, 4]:
                            ending, pos = token.text[-i:], token.forms[0].grams[0]
                            if UnigramMorphAnalyzer.endings_stat.get(ending) is None:
                                # if no such ending
                                UnigramMorphAnalyzer.endings_stat[ending] = {pos: 1}
                            elif UnigramMorphAnalyzer.endings_stat[ending].get(pos) is None:
                                # if no such part of speech
                                UnigramMorphAnalyzer.endings_stat[ending][pos] = 1
                            else:
                                UnigramMorphAnalyzer.endings_stat[ending][pos] += 1


    def predict(self, token):

        if len(token) > 4:
            ending = token[-4:]
        else:
            ending = token

        pos_stat = self.endings_stat[ending]
        total = 0
        for i in pos_stat.values():
            total += i

        return {key: round(value/total, 2) for key, value in pos_stat.items()} # отсортировать по значению


    def save(self):
        with open('morph.pickle', 'wb') as f:
            pickle.dump(self, f)


    def load(self):
        with open('morph.pickle', 'rb') as f:
            return pickle.load(f)


    def eval(self, set):
        pass


def main():
    morph = UnigramMorphAnalyzer()
    morph.train()
    morph.save()


if __name__ == '__main__':
    main()
