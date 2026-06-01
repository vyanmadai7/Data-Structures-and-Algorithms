def longest_unique_substring(s):
    last = {}
    l = 0
    best = 0

    for r in range(len(s)):
        if s[r] in last and last[s[r]] >= l:
            l = last[s[r]] + 1

        last[s[r]] = r
        best = max(best, r - l + 1)

    return best