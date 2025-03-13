import sys
from collections import deque
input = sys.stdin.readline

n, l,r = map(int, input().split())
dir = [[1,0],[-1,0],[0,-1],[0,1]]
area = []
for _ in range(n):
    area.append(list(map(int,input().split())))



cnt = 0

def bfs(i,j):
    q = deque()
    q.append((i,j))
    country = [(i,j)]
    # people = area[i][j]
    while q:
        x, y = q.popleft()
        for di, dj in dir:
            nx, ny = x + di, y+dj
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] ==0: 
                if l <= abs(area[x][y] - area[nx][ny]) <=r:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    country.append((nx,ny))
    return country


while True:
    visited = [[0] * n for _ in range(n)]
    condition = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                                # people += area[nx][ny]
                if len(country) >=2:
                    condition=True
                    result = sum(area[a][b] for a, b in country)//len(country)
                    for cx, cy in country:
                        area[cx][cy] = result
    if not condition:
        break
    cnt += 1
    
print(cnt)
    