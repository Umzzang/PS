import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# area = []
det = {}
for i in range(n):
    lst = list(map(int,input().split()))
    for j in range(len(lst)):
        if lst[j] != 0:
            det[f"{i}s{j}"] = lst[j]
            # print(f"{i}")
    # area.append(lst)
# print(det)
dir = [[1,0],[-1,0],[0,-1],[0,1]]
year = 0
target = []

def change():
    for t in target:
        i,j,cnt = t
        val = det[f"{i}s{j}"]
        # area[i][j] = max(area[i][j]- cnt,0)
        if val - cnt <=0:
            del det[f"{i}s{j}"]
        else:
            det[f"{i}s{j}"] = val- cnt


def cal(i, j, visited):
    stack = []
    stack.append((i,j))
    visited[i][j] = 1
    while stack:
        x, y = stack.pop()
        # t(x,y)
        cnt = 0
        for dx,dy in dir:
            nx,ny = x + dx, y+ dy
            if det.get(f"{nx}s{ny}") and visited[nx][ny] == 0:
                stack.append((nx,ny))
                visited[nx][ny] = 1
            if 0<=nx<n and 0<=ny<m and not det.get(f"{nx}s{ny}"):
                cnt += 1
        target.append((x,y,cnt))
    

def dfs():
    p = 0
    visited = [[0] * m for _ in range(n)]
    if len(det) == 0:
        return p
    for str in det.keys():
        # print(str)
        i, j = map(int ,str.split('s'))
        # print(visited)
        if visited[i][j] == 0:
            p += 1
            if p >= 2:
                return p
            cal(i,j, visited)
    if p == 0:
        return p
    # print("target",target)
    change()
    return p

while 1:
    target = []
    piece = dfs()
    # print(piece)
    if piece >= 2:
        break
    if piece == 0:
        year = 0
        break
    year += 1

print(year)






# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# area = []
# for _ in range(n):
#     area.append(list(map(int,input().split())))

# dir = [[1,0],[-1,0],[0,-1],[0,1]]
# year = 0
# target = []

# def change():
#     for t in target:
#         i,j,cnt = t
#         area[i][j] = max(area[i][j]- cnt,0)


# def cal(i, j, visited):
#     stack = []
#     stack.append((i,j))
#     visited[i][j] = 1
#     while stack:
#         x, y = stack.pop()
#         cnt = 0
#         for dx,dy in dir:
#             nx,ny = x + dx, y+ dy
#             if 0<=nx<n and 0<=ny<m: 
#                 if area[nx][ny] != 0 and visited[nx][ny] == 0:
#                     stack.append((nx,ny))
#                     visited[nx][ny] = 1
#                 if area[nx][ny] == 0:
#                     cnt += 1
#         target.append((x,y,cnt))
    

# def dfs():
#     p = 0
#     visited = [[0] * m for _ in range(n)]
   
#     for i in range(n):
#         for j in range(m):
#             if area[i][j] != 0 and visited[i][j] == 0:
#                 p += 1
#                 if p >= 2:
#                     return p
#                 cal(i,j, visited)
            
#     if p == 0:
#         return p
#     # print("target",target)
#     change()
#     return p

# while 1:
#     target = []
#     piece = dfs()
#     # print(piece)
#     if piece >= 2:
#         break
#     if piece == 0:
#         year = 0
#         break
#     year += 1

# print(year)