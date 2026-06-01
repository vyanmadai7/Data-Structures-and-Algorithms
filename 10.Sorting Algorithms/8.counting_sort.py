def counting_sort(arr):
    if not arr:
        return arr

    m = max(arr)
    count = [0] * (m + 1)

    for num in arr:
        count[num] += 1

    res = []
    for i in range(m + 1):
        res.extend([i] * count[i])

    return res