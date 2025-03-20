import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
area = []
dir = [[0,-1],[0,1],[-1,0],[1,0]]
for _ in range(n):
    area.append(list(map(int, input().split())))

visited = [[-1]*n for _ in range(n)]
answer = 0

def dfs(i,j, c):
    value = 0
    for di, dj in dir:
        ni, nj = i+ di, j+dj
        if 0<=ni<n and 0<=nj<n and area[ni][nj] > area[i][j]:
            if visited[ni][nj] == -1:
                value = max(value, dfs(ni, nj, 1))
                # visited[ni][nj] = value
            else:
                value = max(value, visited[ni][nj])
    
    visited[i][j] = value + c    
    return value + c
    


def pvisit():
    for i in range(n):
        print()
        for j in range(n):
            print(visited[i][j], end=' ')
    print()
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            visited[i][j] = dfs(i, j, 1)
            # print(i,j, visited[i][j])
            # pvisit()
        answer = max(answer, visited[i][j])

print(answer)
