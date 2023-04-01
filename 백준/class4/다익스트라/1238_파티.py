import sys
import heapq
input = sys.stdin.readline

def dij(start):
    dis[start][start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, i = heapq.heappop(q)
        if dis[start][i] < d:
            continue
        for end, time in graph[i]:
            if dis[start][end] > d + time:
                dis[start][end] = d + time
                heapq.heappush(q, (d+time, end))


n, m ,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = 1000000000
dis = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))


for i in range(1, n+1):
    dij(i)

time = []
for i in range(1, n+1):
    time.append(dis[i][x] + dis[x][i])

print(max(time))