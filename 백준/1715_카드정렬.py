import sys
import heapq
input = sys.stdin.readline
n = int(input())

s = 0
numbers = []
# counts = [i for i in range(n-1,-1,-1)]
# counts = [n-1] + counts
for _ in range(n):
    a = int(input())
    heapq.heappush(numbers, a)

while len(numbers)>=2:
    a = heapq.heappop(numbers)
    b = heapq.heappop(numbers)
    heapq.heappush(numbers, a+b)
    s += a+b
print(s)