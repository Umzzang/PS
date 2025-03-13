import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    numbers = list(map(int ,input().split()))
    if not heap:
        for number in numbers:
            heapq.heappush(heap, number)
    else:
        for number in numbers:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
# answer = 0
# for _ in range(n):
#     answer = heapq.heappop(heap)

print(heap[0])