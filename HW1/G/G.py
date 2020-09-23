def solution(a, b):
    new = []
    for el in b:
        if el not in a:
            new.append(el)
    return sorted(a + new)
