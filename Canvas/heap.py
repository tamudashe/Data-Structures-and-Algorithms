import heapq as heap


L = []
heap.heappush(L, 20)
heap.heappush(L, 13)
heap.heappush(L, 7)
heap.heappush(L, 15)
heap.heappush(L, 2)
heap.heappush(L, 10)
heap.heappush(L, 14)

print(L)
print(heap.heappop(L))
print(L)

print(heap.heappushpop(L, 55))
print(L)

L1 = heap.nlargest(3, L)
print(L1)

L2 = heap.nsmallest(3, L)
print(L2)

L3 = [20, 3, 4, 6, 7, 4, 19, 3]
heap.heapify(L3)
print(L3)
