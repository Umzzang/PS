import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
direction = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]

for _ in range(n):
    l = int(input())
    nx, ny = map(int, input().split())
    dx,dy = map(int,input().split())
    vistied = [[0] * l for _ in range(l)]
    q = deque()
    q.append((nx,ny))
    vistied[nx][ny] = 1
    ans = -1
    while q:
        
        x, y = q.popleft()
        if x == dx and y == dy:
            # vistied[ni][nj] = vistied[x][y] + 1
            break
        for di, dj in direction:
            ni, nj = x + di, y + dj
            if 0<= ni <l and 0<=nj<l and vistied[ni][nj] == 0:
                q.append((ni,nj))
                vistied[ni][nj] = vistied[x][y] + 1
    # print(vistied)
    print(vistied[dx][dy] - 1)