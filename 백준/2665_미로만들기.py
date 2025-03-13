import sys
from collections import deque
input = sys.stdin.readline

dir = [[1,0],[-1,0],[0,-1],[0,1]]
area = []
n = int(input())
for _ in range(n):
    area.append(input().rstrip())

q = deque()
visited = [[-1] * n for _ in range(n)]
q.append((0,0))
visited[0][0] = 0
while q:
    x, y = q.popleft()
    for di, dj in dir:
        nx, ny = x +di, y+dj
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
            if area[nx][ny] == '0':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
            else:
                visited[nx][ny] = visited[x][y] 
                q.appendleft((nx,ny))

print(visited[-1][-1])
