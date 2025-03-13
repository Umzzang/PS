import sys

input = sys.stdin.readline

n,m = map(int,input().split())
dir = [[0,-1],[0,1],[-1,0],[1,0]]
pic = []
for _ in range(n):
    pic.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
maxA = 0
stack = []
cnt = 0
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1 and visited[i][j] == 0:
            stack.append((i,j))
            visited[i][j] = 1
            area = 1
            cnt += 1
            while stack:
                x, y = stack.pop()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<n and 0<=ny<m and pic[nx][ny] == 1 and visited[nx][ny] ==0:
                        stack.append((nx,ny))
                        visited[nx][ny] = 1
                        area += 1
            maxA = max(maxA, area)
print(cnt)
print(maxA)

