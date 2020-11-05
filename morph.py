import pickle
from datetime import datetime
from tqdm import tqdm
from corus import load_corpora


class UnigramMorphAnalyzer:

    endings_stat = dict()


    def __init__(self):
        self.endings_stat = UnigramMorphAnalyzer.endings_stat
        self.updated = ''


    def __getitem__(self, key):
        return UnigramMorphAnalyzer.endings_stat[key]


    def __str__(self):
        return f'UnigramMorphAnalyzer object, latest update: {self.updated}'


    def train(self, train_set):

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


    def predict(self, token):

        n = 4
        while n >= 1:
            try:
                ending = token[-n:]
                pos_stat = self.endings_stat[ending]
                total = 0
                for i in pos_stat.values():
                    total += i
                return {round(value / total, 2): key for key, value in pos_stat.items()}
            except:
                n -= 1
                continue
        return {1.0: 'UNKN'}


    def save(self):
        with open('morph.pickle', 'wb') as f:
            pickle.dump(self, f)


    def load(self):
        with open('morph.pickle', 'rb') as f:
            return pickle.load(f)


    def eval(self, test_set):

        P = 0 # tokens for which pos recognition was correct
        N = 0 # all tokens
        for token in test_set:
            predicted = self.predict(token[0])
            if predicted[max(predicted.keys())] == token[1]:
                P += 1
            N += 1
        return ('accuracy', P / N)



def train_test_split(records, train_size=0.8):
    data = []

    for rec in tqdm(records):
        for par in rec.pars:
            for sent in par.sents:
                for token in sent.tokens:
                    for i in [1, 2, 3, 4]:
                        data.append((token.text[-i:], token.forms[0].grams[0]))

    n = int(len(data) * train_size)
    train_set, test_set = data[:n], data[n:]

    return train_set, test_set


def main():
    records = load_corpora('/Users/aleontyev/annot.opcorpora.xml.byfile.zip')
    train_set, test_set = train_test_split(records)

    a = UnigramMorphAnalyzer()
    a.train(train_set)
    a.save()

    b = UnigramMorphAnalyzer().load()
    print(b.eval(test_set))


if __name__ == '__main__':
    main()
