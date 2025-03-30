import sys

input = sys.stdin.readline

dir = [[-1,0],[0,1],[1,0],[0,-1]] # 북 동 남 서
n, m = map(int, input().split())
room = []  # 1 벽 0 not청소 2 청소된 방j
cnt = 0

def direction(d):
    if d<0:
        return d + 4
    else:
        return d

def robot(i,j,d):
    global cnt
    if room[i][j] == 0:
        cnt += 1
        room[i][j] = 2
    possible = 0
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0<=ni<n and 0<=nj<m and room[ni][nj] == 0:
            possible = 1
            break
    if possible:
        nd = direction(d-1)
        while True:
            ni = i + dir[nd][0]
            nj = j + dir[nd][1]
            if 0<= ni<n and 0<=nj<m and room[ni][nj] == 0:
                robot(ni, nj,nd)
                break
            else:
                nd = direction(nd-1)

    else:
        nd = direction(d-2)
        ni = i + dir[nd][0]
        nj = j + dir[nd][1]
        if 0<= ni<n and 0<=nj<m and room[ni][nj] != 1:
            robot(ni, nj, d)
        else:
            return

x,y,d = map(int, input().split())
for _ in range(n):
    room.append(list(map(int,input().split())))

robot(x,y,d)
print(cnt)
