import bisect

def lis(nums):
    res = []

    for x in nums:
        idx = bisect.bisect_left(res, x)
        if idx == len(res):
            res.append(x)
        else:
            res[idx] = x

    return len(res)