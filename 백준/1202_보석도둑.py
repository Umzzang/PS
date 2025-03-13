import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
juw = []
bags = []
answer = 0
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(juw, (m,v))

for _ in range(k):
    bags.append(int(input()))

bags.sort()
temp = []
for bag in bags:
    while juw and bag >= juw[0][0]:
        heapq.heappush(temp, -heapq.heappop(juw)[1])
    if temp:
        answer -= heapq.heappop(temp)
    elif not juw:
        break


print(answer)
