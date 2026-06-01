s = "abcabcbb"

seen = {}
start = max_len = 0

for end, char in enumerate(s):
    if char in seen and seen[char] >= start:
        start = seen[char] + 1
    seen[char] = end
    max_len = max(max_len,end - start + 1)

print(max_len)

#Time complexity: O(n)
#Space complexity: O(min(n,charset))