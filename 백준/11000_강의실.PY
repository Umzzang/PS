import sys
import heapq
input = sys.stdin.readline

n = int(input())

times = []
for _ in range(n):
    s, e = map(int ,input().split())
    heapq.heappush(times, (s, e))

cnt = 0
tmp = []
while times:
    s, e = heapq.heappop(times)
    # print(tmp)
    if tmp:
        if tmp[0] <= s:
            heapq.heappop(tmp)
            heapq.heappush(tmp, e)
        else:
            heapq.heappush(tmp, e)
    else:
        heapq.heappush(tmp, e)
        cnt += 1
# print(tmp)
print(len(tmp))
