import sys
import heapq

input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = 1000000000


def dij(start):
    dis = [inf] * (n+1)
    dis[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        t, i = heapq.heappop(q)
        if dis[i] < t:
            continue
        for node, time in graph[i]:
            if dis[node] > time + dis[i]:
                dis[node] = time + dis[i]
                heapq.heappush(q, (time, node))


    return dis


for _ in range(e):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    graph[end].append((start, time))

v1, v2 = map(int, input().split())

dis1 = dij(1)
dis2 = dij(v1)
dis3 = dij(v2)



a = dis1[v1] + dis2[v2] +dis3[n]
b = dis1[v2] + dis3[v1] + dis2[n]
c = min(a, b)
if c >= inf:
    print(-1)
else:
    print(c)

# print(dis[n])
