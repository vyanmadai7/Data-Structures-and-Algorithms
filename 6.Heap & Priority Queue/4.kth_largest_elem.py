import heapq

def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for n in nums[k:]:
        if n > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, n)

    return heap[0]

print(findKthLargest([3, 2, 1, 5, 6, 4], 2))