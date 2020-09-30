def solution(n, k):
    # свое решение через списки: доходит до 55 теста, но не проходит по времени
    data = list(range(1, n+1))
    num = 0
    while len(data) > 1:
        current = tuple(data.copy())
        for el in current:
            if el == data[0] and el == data[-1]:
                break
            else:
                num += 1
                if num == k:
                    del data[data.index(el)]
                    num = 0
    return data[0]


def solution2(n, k):
    # нагугленное решение, но работает быстро
    res = 0
    for i in range(1, n + 1):
        res = (res + k) % i

    return res + 1
