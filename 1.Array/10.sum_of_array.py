def sum_array(arr):
    total = 0 
    for num in arr:
        total += num
    return total

arr = [10,20,30,40,50]
print(sum_array(arr))

#Time complexity: O(n)
#Space complexity: O(1)