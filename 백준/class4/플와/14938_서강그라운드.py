import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
inf = 100000000
graph = [[inf] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(r):
    s, e, c = map(int, input().split())
    graph[s][e] = c
    graph[e][s] = c

dis = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i != k:
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
                
for i in range(1, n+1):
    dis[i] += item[i]
    for j in range(1, n+1):
        if i != j and graph[i][j] <= m:
            dis[i] += item[j]

# print(dis)
print(max(dis))