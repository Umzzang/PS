import sys
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def search(i, j):
    global m, n, visited
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        area[x][y] = 2
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0<=nx<m and 0<=ny<n and area[nx][ny] == 1:
                stack.append((nx, ny))



t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split(' '))
    area = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        i, j = map(int, input().split(' '))
        area[i][j] = 1
    for i in range(m):
        for j in range(n):
            if area[i][j] == 1:
                
                search(i,j)
                cnt += 1
    print(cnt)