def solution(x):
    y = x[0]
    for i in range(1, len(x)):
        if i % 3 != 0:
            if x[i] == 'h':
                if i != x.find('h') and i != x.rfind('h'):
                    y += 'H'
                else:
                    y += 'h'
            else:
                y += x[i]

    answer = y.replace('1', 'one')
    return answer


