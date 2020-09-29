def solution(arr):
    if len(arr) == 0:
        return []

    new = []
    current = tuple(arr)

    for i in range(len(current)):
        if i == 0: # если верхняя строка
            new.extend(current[i])
            del arr[arr.index(current[i])]
        elif i == len(current) - 1: # если нижняя строка
            new.extend(list(reversed(current[i])))
            del arr[arr.index(current[i])]
        else: # ползем вниз по правому краю
            new.append(current[i][-1])
            del arr[arr.index(current[i])][-1]

    for i in reversed(range(len(current))): # ползем вверх по левому краю
        new.append(current[i][0])
        del arr[arr.index(current[i])][0]

    return new + solution(arr)