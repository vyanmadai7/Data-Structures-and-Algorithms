arr = [1,2,3,4,5]

arr2 = [1,2,3,4,5]
left, right = 0, len(arr2) - 1
while left < right:
    arr2[left], arr2[right] = arr2[right], arr2[left]
    left += 1
    right -= 1
print(arr2)