import pickle


class UnigramMorphAnalyzer:

    endings_stat = dict()

    def __init__(self):
        pass


    def train(self, set):
        pass


    def predict(self, set):
        pass


    def save(self):
        with open(f'{self}.pickle', 'w') as f:
            pickle.dump(self, f)


    def load(self):
        with open(f'{self}.pickle', 'w') as f:
            return pickle.load(f)


    def eval(self):
        pass