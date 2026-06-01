#Kadane's Algorithm

nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = float("-inf")
current_sum = 0

for num in nums:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print("Maximum subarray sum: ", max_sum)

#Time complexity: O(n)
#Space complexity: O(1)