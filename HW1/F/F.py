def solution(n):
    i = 0
    answ = [1]
    while True:
        if answ[i] > n:
            del(answ[i])
            return answ
        else:
            answ.append(answ[i]*2)
            i += 1