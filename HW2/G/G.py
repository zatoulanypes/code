def solution(a, b):
    new = a + [el for el in b if el not in a]
    answer = []
    while bool(new):
        i = min(new)
        answer.append(i)
        del new[new.index(i)]

    return answer
