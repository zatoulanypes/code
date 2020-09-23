def solution(total):

    if total < 1440:
        h = total // 60
        m = total % 60

    elif total > 1440:
        total -= 1440 * (total // 1440)
        h = total // 60
        m = total % 60

    else:
        h = 0
        m = 0

    return str(h) + ' ' + str(m)
