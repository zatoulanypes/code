def solution(n):
    if n > 0:
        penguins = '   _~_   ' * n + '\n' + \
                  '  (o o)  ' * n + '\n' + \
                  ' /  V  \ ' * n + '\n' + \
                  '/(  _  )\\' * n + '\n' + \
                  '  ^^ ^^  ' * n
    else:
        penguins = ''
    return (penguins)
