def integers():
    i = 1
    while True:
        yield i
        i += 1
       
   
def squares():
    for i in integers():
        yield i*i
       
   
def take(n, generator):
    return [next(generator) for i in range(n)]
