import sys
input = sys.stdin.readline

n, m = map(int, input().split())
area = []
camera = []

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] != 0 and lst[j] !=6:
            camera.append((lst[j],i,j))
    area.append(lst)
answer = n * m

direction = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]],
}

def detect(area, d, i, j):
    if d == 0:
        for k in range(i-1, -1, -1):
            if area[k][j] == 0:
                area[k][j] = '#'
            elif area[k][j] == 6:
                return
    elif d == 1:
        for k in range(j+1, m):
            if area[i][k] == 0:
                area[i][k] = '#'
            elif area[i][k] == 6:
                return
    elif d == 2:
        for k in range(i+1, n):
            if area[k][j] == 0:
                area[k][j] = '#'
            elif area[k][j] == 6:
                return
    else:
        for k in range(j-1, -1, -1):
            if area[i][k] == 0:
                area[i][k] = '#'
            elif area[i][k] == 6:
                return



def count_zera(area):
    global answer
    cnt = 0
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == 0:
                cnt += 1
    
    answer = min(answer, cnt)

def dfs(level, area):
    
    if level == len(camera):
        return count_zera(area)

    num, i, j = camera[level]
    copy_area = [[j for j in area[i]] for i in range(n)]

    for d in direction[num]:
        for dd in d:
            detect(copy_area, dd,i,j)
        dfs(level+1, copy_area)
        copy_area = [[j for j in area[i]] for i in range(n)]


dfs(0, area=area)
print(answer)

