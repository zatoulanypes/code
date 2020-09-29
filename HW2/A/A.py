def solution(arr):
    if len(arr) > 0:
        current = 1
        biggest = 1

        that = arr[0]
        for this in arr[1:]:
            if this == that:
                current += 1
            else:
                current = 1

            if current > biggest:
                biggest = current

            that = this

    return biggest
