import sys
import heapq
#1273 최단경로

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
inf = 1000000000
graph = [[] for _ in range(v+1)]

dis = [inf] * (v+1)
visited = [0] * (v+1)

def get_small():
    maxV = inf
    index = 0
    for i in range(1, v+1):
        if visited[i] == 0 and dis[i] < maxV:
            maxV = dis[i]
            index = i
    return index


def dij(i):
    dis[i] = 0
    visited[i] = 1
    for end, d in graph[i]:
        dis[end] = d

    for _ in range(v-1):
        now = get_small()
        visited[now] = 1
        for end, d in graph[now]:
            if dis[end] > dis[now] + d:
                dis[end] = dis[now] + d


def dij2(i):
    dis[i] = 0
    q = []
    heapq.heappush(q, (0, i))
    while q:
        distance, node = heapq.heappop(q)
        if dis[node] < distance:
            continue
        for end, d in graph[node]:
            if dis[end] > d + dis[node]:
                dis[end] = d + dis[node]
                heapq.heappush(q, (d+dis[node], end))


for i in range(e):
    s, end, w = map(int, input().split())
    graph[s].append((end, w))



# dij(k)
dij2(k)

for i in range(1, v+1):
    if dis[i] == inf:
        print('INF')
    else:
        print(dis[i])