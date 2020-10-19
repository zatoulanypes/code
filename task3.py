def integers():
    i = 1
    while True:
        yield i
        i += 1
       
   
def squares():
    for i in integers():
        yield i*i


def take(n, generator):
    res = []
    try:
        for i in range(n):
            res.append(next(generator))
    except StopIteration:
        pass
    return res