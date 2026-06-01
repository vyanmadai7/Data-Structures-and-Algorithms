nums = [2, 7, 11, 15]
target = 9

num_to_index = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in num_to_index:
        print([num_to_index[complement],i])
        break
    num_to_index[num] = i 

#Time complexity: O(n)
#Space complexity: O(n)
