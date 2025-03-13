import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0

q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

def r(q:deque):
    newq = deque()
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and tomato[ni][nj] == 0:
                newq.append((ni,nj))
                tomato[ni][nj] = 1
    return newq

while True:
    q = r(q)
    if not q:
        break
    cnt += 1

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            cnt = -1 
            break
    if cnt == -1:
        break
print(cnt)