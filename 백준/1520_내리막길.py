import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

dir = [[0,-1],[0,1],[-1,0],[1,0]]
m, n = map(int,input().split())
area = []
for _ in range(m):
    area.append(list(map(int, input().split())))

answer= 0
# def bfs(i,j):
#     global answer
#     if i == m-1 and j == n-1:
#         answer += 1
#     for dx, dy in dir:
#         nx, ny = i+ dx, j+dy
#         if 0<=nx<m and 0<=ny<n and area[nx][ny] < area[i][j] and visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             bfs(nx,ny)
#             visited[nx][ny] = 0
# visited = [[0] * n for _ in range(m)]
# visited[0][0] = 1

dp = [[-1] * n for _ in range(m)]
def bfs(i,j):   # 
    if i == m-1 and j == n-1:
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]
    ways = 0
    for di, dj in dir:
        ni, nj = i +di, j+dj
        if 0<=ni<m and 0<=nj<n and area[ni][nj] < area[i][j]:
            ways += bfs(ni,nj)
    dp[i][j] = ways
    return ways

bfs(0,0)
# print(dp)
print(dp[0][0])