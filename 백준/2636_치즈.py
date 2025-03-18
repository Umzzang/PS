import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cheese = []
for i in range(n):
    cheese.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
firstcheese = 0
for i in range(n):
    for j in range(m):
        if cheese[i][j] == 1:
            firstcheese += 1

def makeout(i,j):
    # cheese[i][j] = -1
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()
        cheese[x][y] = -1
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m and cheese[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1

def check():
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                return True
    else:
        return False

def air():
    delete = []
    cheesecnt = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                cheesecnt += 1
                for di, dj in dir:
                    ni, nj = i +di, j+dj
                    if 0<=ni<n and 0<=nj<m and cheese[ni][nj] == -1:
                        delete.append((i,j))
                        break
    deletecnt = 0
    for dx, dy in delete:
        deletecnt += 1
        makeout(dx, dy)
        # cheese[dx][dy] = -1

    # for dx, dy in delete:

    return cheesecnt - deletecnt

for i in range(n):
    if i == 0 or i == n-1:
        for j in range(m):
            if visited[i][j] == 0:
                makeout(i,j)
    else:
        if j == 0 or j == m-1:
            if visited[i][j] == 0:
                makeout(i,j)

hour = 0
restlst = []
while check():
    hour += 1
    rest = air()
    restlst.append(rest)

print(hour)
# print(restlst)
if len(restlst) > 1:
    print(restlst[-2])
else:
    print(firstcheese)