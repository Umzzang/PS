import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, c = map(int, input().split())
    tree[s].append((e, c))
    tree[e].append((s, c))

maxv = 0

def search(i):
    global maxv
    visited = [0] * (n+1)
    visited[i] = 1
    now = i
    q = deque()
    q.append((i, 0))
    while q:
        node, c = q.popleft()
        visited[node] = 1
        if c > maxv:
            maxv = c
            now = node
        for end, cost in tree[node]:
            if visited[end] == 0:
                q.append((end, c + cost))
    return now, maxv

index, maxV = search(1)
index, maxV = search(index)
print(maxV)