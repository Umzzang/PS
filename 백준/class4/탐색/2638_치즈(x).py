import sys
from collections import deque

input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
def air(i, j):
    
    stack = [(i, j)]
   
    while stack:
        i, j = stack.pop()
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0 and visited[ni][nj] == -1:
                stack.append((ni, nj))
                visited[ni][nj] = 0


   

def cheese():
    airlst = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                
                cnt = 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 0 and visited[ni][nj] != -1:
                        cnt += 1
                if cnt >= 2:
                    airlst.append((i, j))
                    visited[i][j] = 1
                    
                
    print(visited)
                    
    print(airlst)
    

    while airlst:
        i, j = airlst.popleft()
        arr[i][j] = 0
        air(i, j)
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 1:
                cnt = 0
                for ddi, ddj in d:
                    nni, nnj = ni + ddi, nj + ddj
                    if 0<=nni<n and 0<=nnj<m and arr[nni][nnj] == 0 and visited[nni][nnj] != -1:
                        cnt += 1
                if cnt >= 2:
                    visited[ni][nj] = visited[i][j] + 1
                    airlst.append((ni, nj))
                    
    

    



air(0, 0)
for i in range(n):
    print(*visited[i])
print()
for i in range(n):
    print(*arr[i])
print()
# print(arr)
cheese()

    
for i in range(n):
    print(*visited[i])
print()
for i in range(n):
    print(*arr[i])    


