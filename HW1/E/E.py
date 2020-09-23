import random

def solution(x1, y1, x2, y2):
    for i in range(x1-1, x1+2):
        for j in range(y1-1, y1+2):
            if (i, j) == (x2, y2):
                return True
    return False