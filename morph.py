import pickle
from datetime import datetime
from tqdm import tqdm
from corus import load_corpora


class UnigramMorphAnalyzer:

    records = load_corpora('annot.opcorpora.xml.byfile.zip')
    endings_stat = dict()


    def __init__(self):
        self.endings_stat = UnigramMorphAnalyzer.endings_stat
        self.updated = ''


    def __getitem__(self, key):
        return UnigramMorphAnalyzer.endings_stat[key]


    def __str__(self):
        return f'UnigramMorphAnalyzer object, latest update: {self.updated}'


    def train(self):
        # SPLITTING DATA IN TRAIN / TEST SETS
        data = []
        for rec in tqdm(UnigramMorphAnalyzer.records):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        for i in [1, 2, 3, 4]:
                            data.append((token.text[-i:], token.forms[0].grams[0]))
        n = int(len(data) * 0.8)
        train_set, test_set = data[:n], data[n:]

        # TRAINING
        for ending, pos in tqdm(train_set):
            if UnigramMorphAnalyzer.endings_stat.get(ending) is None:
                # if no such ending
                UnigramMorphAnalyzer.endings_stat[ending] = {pos: 1}
            elif UnigramMorphAnalyzer.endings_stat[ending].get(pos) is None:
                # if no such part of speech
                UnigramMorphAnalyzer.endings_stat[ending][pos] = 1
            else:
                UnigramMorphAnalyzer.endings_stat[ending][pos] += 1

        self.updated = datetime.isoformat(datetime.now(), sep=' ')
        return test_set


    def predict(self, token):

        try:
            if len(token) > 4:
                ending = token[-4:]
            else:
                ending = token

            pos_stat = self.endings_stat[ending]
            total = 0
            for i in pos_stat.values():
                total += i

            return {round(value/total, 2): key for key, value in pos_stat.items()}

        except KeyError:
            return {1.0: 'UNKN'}


    def save(self):
        with open('morph.pickle', 'wb') as f:
            pickle.dump(self, f)


    def load(self):
        with open('morph.pickle', 'rb') as f:
            return pickle.load(f)


    def eval(self):

        P = 0 # tokens for which pos recognition was correct
        N = 0 # all tokens
        for token in self.train():
            predicted = self.predict(token[0])
            if predicted[max(predicted.keys())] == token[1]:
                P += 1
            N += 1
        return ('accuracy', P / N)


def main():
    a = UnigramMorphAnalyzer()
    print(a)
    print(a.eval())
    print(a)
    a.save()

    b = UnigramMorphAnalyzer().load()
    print(b)
    print(b.predict('запрет'))


if __name__ == '__main__':
    main()
