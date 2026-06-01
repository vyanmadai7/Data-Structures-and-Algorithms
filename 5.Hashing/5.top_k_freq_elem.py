from collections import Counter
import heapq

def top_k_frequent(nums,k):
    freq = Counter(nums)
    return heapq.nlargest(k,freq.keys(),key=freq.get)

nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums,k))