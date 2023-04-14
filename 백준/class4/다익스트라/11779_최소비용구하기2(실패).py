import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

inf = 1000000000

graph = [[inf] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s][e] = c

s, e = map(int, input().split())


def dij(start):
    dis = [[inf, []] for _ in range(n+1)]
    dis[start][0] = 0
    
    
    q = []
    heapq.heappush(q, (0, start, [start]))
    while q:
        
        cost, i, p = heapq.heappop(q)

        if cost > dis[i][0]:
            continue

        for j in range(1, n+1):
            
            if dis[j][0] > cost + graph[i][j]:
                dis[j][0] = cost + graph[i][j]
                dis[j][1] = p + [j]
                
                heapq.heappush(q, (cost + graph[i][j], j, p + [j]))

    return dis
result = dij(s)
# print(result)
print(result[e][0])
print(len(result[e][1]))
print(*result[e][1])