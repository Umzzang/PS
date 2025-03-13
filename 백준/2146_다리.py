import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
dir = [[0,-1],[0,1],[-1,0],[1,0]]
area = []
for _ in range(n):
    area.append(list(map(int,input().split())))

island = []

def bfs(i,j, cnt):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        area[x][y] = cnt
        for dx, dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and area[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1

visited = [[0] * n for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if area[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j, cnt)
            cnt += 1


def bfs2(i,j,num):
    dis = 10002
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((i,j,0))
    visited[i][j] = 1
    while q:
        x, y, d = q.popleft()
        if area[x][y] != num and area[x][y] != 0:
            return d-1
        for dx, dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and area[nx][ny] != num and visited[nx][ny] == 0:
                q.append((nx,ny,d+1))
                visited[nx][ny] = 1
    return dis

    

answer = 10002
for island in range(1, cnt):
    for i in range(n):
        for j in range(n):
            if area[i][j] == island:
                answer = min( answer, bfs2(i,j,island))
print(answer)
