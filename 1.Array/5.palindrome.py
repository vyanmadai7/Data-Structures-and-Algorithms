s = "racecar"

left, right = 0,  len(s) - 1
is_palind = True
while left < right:
    if s[left] != s[right]:
        is_palind = False
        break
    left += 1
    right -= 1
print(is_palind)

#Time complexity: O(n)
#Space complexity: O(1)

