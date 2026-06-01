import heapq

heap = []
heapq.heappush(heap,5)
heapq.heappush(heap,1)
heapq.heappush(heap,3)

print("Heap: ", heap)
print("Min element: ",heap[0])

print("Pop: ",heapq.heappop(heap))
print("Heap after pop: ", heap)