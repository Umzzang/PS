import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 1000000000
bus = [[] for _ in range(n+1)]
dis = [inf] * (n+1)


def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        cost, cur = heapq.heappop(q)
        if dis[cur] < cost:
            continue

        for next, nextc in bus[cur]:
            if dis[next] > cost + nextc:
                dis[next] = cost + nextc
                heapq.heappush(q, (cost+nextc, next))

for _ in range(m):
    s, e, c = map(int, input().split())
    bus[s].append((e, c))
s, e = map(int, input().split())

dij(s)

print(dis[e])