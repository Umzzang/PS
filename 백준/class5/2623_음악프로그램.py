# 위상정렬 다시보자

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [0] * (n+1)

link = [[] for _ in range(n+1)]
link2 = [[] for _ in range(n+1)]
result = []
for _ in range(m):
    l = list(map(int, input().split()))
    for i in range(len(l)-1, 1, -1):
        link[l[i]].append(l[i-1])
        link2[l[i-1]].append(l[i])

# print(link)
degree = [len(link[i]) for i in range(n+1)]
# print(degree)
# print(link2)

q = deque()
for i in range(1, len(degree)):
    if degree[i] == 0 and visited[i] == 0:
        q.append(i)
        visited[i] = 1

while q:
    i = q.popleft()
    if degree[i] == 0:
        result.append(i)
    for k in link2[i]:
        degree[k] -= 1
        if degree[k] <= 0:
            q.append(k)
            visited[k] = 0

if sum(degree) == 0:
    for i in range(len(result)):
        print(result[i])
else:
    print(0)
    



