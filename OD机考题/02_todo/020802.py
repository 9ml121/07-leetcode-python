
import heapq

n = int(input())
times = int(input())
minHeap = []

for i in range(n):
    endTime, score = map(int, input().split())
    if len(minHeap) < endTime and len(minHeap) < times:
        heapq.heappush(minHeap, score)
    else:
        heapq.heappop(minHeap)
        heapq.heappush(minHeap, score)

print(sum(minHeap))

    
