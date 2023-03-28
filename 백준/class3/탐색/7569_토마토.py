import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0

tomato = []
for _ in range(h):
    t = []
    for _ in range(n):
        a = list(map(int, input().split()))
        b = [0] * m
        a = list(zip(a, b))
        t.append(a)
    tomato.append(t)

# print(tomato)

# while r:
#     pass


def once(q:deque):
    newq = deque()
    while q:
        i, j, k = q.popleft()
        di = i - 1
        ui = i + 1
        if 0<=di<h and tomato[di][j][k][0] == 0 and tomato[di][j][k][1] == 0:
            newq.append((di, j, k))
            tomato[di][j][k] = (1, 1)
        if 0<=ui<h and tomato[ui][j][k][0] == 0 and tomato[ui][j][k][1] == 0:
            newq.append((ui, j, k))
            tomato[ui][j][k] = (1, 1)
        for dj, dk in d:
            nj, nk = j + dj, k + dk
            if 0<=nj<n and 0<=nk<m and tomato[i][nj][nk][0] == 0 and tomato[i][nj][nk][1] == 0:
                newq.append((i, nj, nk))
                tomato[i][nj][nk] = (1, 1)

    return newq

q = deque()

for i in range(h):    
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k][0] == 1:
                q.append((i, j, k))


while True:
    
    q = once(q)
    if not q:
        break
    cnt += 1


for i in range(h):    
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k][0] == 0:
                cnt = -1
                break
        if cnt == -1:
            break
    if cnt == -1:
        break


print(cnt)