import sys
from collections import deque
# bfs
input = sys.stdin.readline

n, m = map(int,input().split())
dir = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(i,j,time):
    ans = 0
    q = deque()
    q.append((i,j, time))
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    while q:
        x, y, t = q.popleft()
        ans = max(t, ans)
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m and area[nx][ny] == 'L' and visited[nx][ny] == 0:
                q.append((nx,ny, t+1))
                visited[nx][ny] = 1
    return ans

answer = 0
area = []
for _ in range(n):
    area.append(input().rstrip())
# print(area)
for i in range(n):
    for j in range(m):
        if area[i][j] == 'L':
            answer = max(bfs(i,j,0), answer)
print(answer)


# import sys
# input = sys.stdin.readline

# def main():
#     n, m = map(int, input().split())
#     graph = [input().rstrip() for _ in range(n)]
#     dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     visited = [[0] * m for _ in range(n)]
#     dist = 0
#     pos = []
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 'L' and not visited[i][j]:
#                 visited[i][j] = 1
#                 q = [(i, j, 0)]
#                 while q:
#                     y, x, d = q.pop(0)
#                     if d > dist:
#                         print(y, x, d)
#                         dist = d
#                         pos.append((y, x))
#                     for dy, dx in dyx:
#                         ny, nx = y + dy, x + dx
#                         if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 'L' and not visited[ny][nx]:
#                             visited[ny][nx] = 1
#                             q.append((ny, nx, d + 1))
#     ans = 0
#     for i, j in pos:
#         visited = [[0] * m for _ in range(n)]
#         visited[i][j] = 1
#         q = [(i, j, 0)]
#         while q:
#             y, x, d = q.pop(0)
#             if d > ans: ans = d
#             for dy, dx in dyx:
#                 ny, nx = y + dy, x + dx
#                 if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 'L' and not visited[ny][nx]:
#                     visited[ny][nx] = 1
#                     q.append((ny, nx, d + 1))
#     print(ans)

# main()