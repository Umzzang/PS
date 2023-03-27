import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def search(i, j):
    global cnt
    cnt += 1
    house = 0
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        
        house += 1
        for di, dj in d:
            ni = x + di
            nj = y + dj
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1
    return house

house = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            house.append(search(i, j))

print(cnt)
house.sort()
for h in house:
    print(h)