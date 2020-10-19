class reverse_iter:
    def __init__(self, lst):
        self.i = 1
        self.n = len(lst)
        self.lst = lst


    def __iter__(self):
        return self


    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return self.lst[-i]
        else:
            raise StopIteration()
