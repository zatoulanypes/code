class OneIndexedList():
    def __init__(self, items):
        self.items = list(items)

    def __getitem__(self, index):
        return self.items[index-1]

    def __setitem__(self, index, value):
        self.items[index-1] = value
