import heapq

max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -3)

print("Max element: ", -max_heap[0])
print("Pop Element: ", -heapq.heappop(max_heap))

heapq.heapify(max_heap)