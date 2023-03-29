import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
visitedgb = [[0] * n for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def s(i, j, c):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for di, dj in d:
            nx, ny = x + di, y +dj
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == c and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

def sgb(i, j, c):
    q = deque()
    q.append((i, j))
    visitedgb[i][j] = 1
    while q:
        x, y = q.popleft()
        for di, dj in d:
            nx, ny = x + di, y +dj
            if c == 'B':
                if 0<=nx<n and 0<=ny<n and arr[nx][ny] == c and visitedgb[nx][ny] == 0:
                    q.append((nx, ny))
                    visitedgb[nx][ny] = 1
            else:
                if 0<=nx<n and 0<=ny<n and (arr[nx][ny] == 'G' or arr[nx][ny] == 'R') and visitedgb[nx][ny] == 0:
                    q.append((nx, ny))
                    visitedgb[nx][ny] = 1
        


cnt = 0
cntgb = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            s(i, j, arr[i][j])
            cnt += 1
        if visitedgb[i][j] == 0:
            sgb(i, j, arr[i][j])
            cntgb += 1

print(cnt, cntgb)
