def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    res = []
    last_end = float('-inf')

    for s, e in intervals:
        if s >= last_end:
            res.append((s, e))
            last_end = e

    return res