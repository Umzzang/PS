import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]

d = [(1, 0),(-1, 0), (0,1), (0,-1)]
visited = [[-1] * m for _ in range(n)]
maxv = 0
def air(i, j):
    stack = deque()
    stack.append((i, j))
    visited[i][j] = 0
    arr[i][j] = 0
    while stack:
        i, j = stack.pop()
        
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == arr[i][j] and visited[ni][nj] == -1:
                stack.append((ni, nj))
                visited[ni][nj] = 0


def cheese(change):               
    # print(change)
    new_lst = []
    # for i in range(n):
    #     print(*visited[i])
    # print()
    for i, j in change:
        air(i, j)
    # for i in range(n):
    #     print(*visited[i])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt = 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0 and visited[ni][nj] != -1:
                        cnt += 1
                if cnt >= 2:
                    new_lst.append((i, j))
    return list(set(new_lst))

                    

air(0, 0)
lst = []
for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt = 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0 and visited[ni][nj] != -1:
                        cnt += 1
                if cnt >= 2:
                    lst.append((i, j))

time = 0 
while True:
    time += 1
    lst = cheese(lst)
    if not lst:
        break
print(time)