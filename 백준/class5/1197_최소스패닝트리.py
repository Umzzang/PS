import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

graph = []
visited = [i for i in range(v+1)]


def find_root(x):
    if visited[x] == x:
        return x
    else:
        visited[x] = find_root(visited[x])
        return visited[x]



def union_root(x, y):
    x = find_root(x)
    y = find_root(y)

    if x != y:
        if x < y:
            visited[y] = x
        else:
            visited[x] = y


for _ in range(e):
    s, e, c = map(int, input().split())
    heapq.heappush(graph, (c, s, e))

v = 0
while graph:
    c, s, e = heapq.heappop(graph)
    if find_root(s) != find_root(e):
        v += c
        union_root(s, e)

print(v)