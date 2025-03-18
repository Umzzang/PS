import sys
input = sys.stdin.readline

dir =[[1,0],[1,1],[1,-1],[0,1],[0,-1],[0,0],[-1,0],[-1,-1],[-1,1]]
w, h= map(int,input().split())

while w or h:
    area = []
    for _ in range(h):
        area.append(list(map(int, input().split())))
    visited = [[0] * w for _ in range(h)] 
    cnt = 0
    q = []
    for i in range(h):
        for j in range(w):
            if area[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    x, y = q.pop()
                    for dx, dy in dir:
                        nx, ny = x +dx,y+dy
                        if 0<=nx<h and 0<=ny<w and area[nx][ny] == 1 and visited[nx][ny] == 0:
                            q.append((nx,ny))
                            visited[nx][ny] = 1
    print(cnt)
    w, h = map(int, input().split())
    
