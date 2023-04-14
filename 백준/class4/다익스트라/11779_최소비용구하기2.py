import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

inf = 1000000000

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

s, e = map(int, input().split())

def dij(start):
    dis = [[inf, []] for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start, [start]))
    while q:
        cost, end, p = heapq.heappop(q)
        if cost > dis[end][0]:
            continue
        for e, c in graph[end]:
            if cost + c < dis[e][0]:
                dis[e][0] = cost + c
                dis[e][1] = p + [e]
                heapq.heappush(q, (cost+c, e, p + [e]))

    return dis


result = dij(s)
print(result[e][0])
print(len(result[e][1]))
print(*result[e][1])