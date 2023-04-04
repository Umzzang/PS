import sys

input = sys.stdin.readline

d = [(1, 0), (-1, 0),(0, 1), (0, -1)]
n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)] 
cnt = 0
w = []
dd = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == '*':
            w.append((i, j))
        if arr[i][j] == 'S':
            dd.append((i, j))
            visited[i][j] = 1

def water(w: list):
    for k in range(len(w)):
        i, j = w[k]
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj] == '.':
                arr[ni][nj] = '*'
                w.append((ni, nj))
    return w

def escape(dd):
    new_dd = []
    while dd:
        
        i, j = dd.pop()
        for di, dj in d:
            ni, nj = di + i, dj + j
            if 0<=ni<n and 0<=nj<m:
               
                if arr[ni][nj] == 'D':
                    return 1
                if arr[ni][nj] != 'X' and arr[ni][nj] != '*' and visited[ni][nj] == 0:
                    new_dd.append((ni, nj))
                    visited[ni][nj] = 1
   
    return new_dd
a = 0
while True:
    cnt += 1
    w = water(w)
    # print(w)
    dd = escape(dd)
    # print(dd)
    if dd == 1:
        break
    elif dd == []:
        a = 1
        break

if a == 1:
    print('KAKTUS')
else:
    print(cnt)