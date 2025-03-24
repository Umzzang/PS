# import sys
# from collections import deque
# input = sys.stdin.readline

# dir = [[1,0],[-1,0],[0,1],[0,-1]]
# n, k = map(int, input().split())
# area = []
# for _ in range(n):
#     area.append(list(map(int,input().split())))


# # virus = [[] for _ in range(k+1)]




# s,tx,ty = map(int, input().split())

# # for _ in range(s):
# #     newvirus = [[] for _ in range(k+1)]
# #     for i in range(len(virus)):
# #         for x, y in virus[i]:
# #             for di, dj in dir:
# #                 ni, nj = x + di, y + dj
# #                 if 0<=ni<n and 0<=nj<n and area[ni][nj] == 0:
# #                     newvirus[i].append((ni,nj))
# #                     area[ni][nj] = i
# #     for i in range(len(virus)):
# #         virus[i] += newvirus[i]


# visited = [[-1] *n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if area[i][j] != 0:
#             visited[i][j] = 0

# # print(visited)
# for i in range(n):
#     for j in range(n):
#         q=deque()
#         if visited[i][j] == 0:
#             q.append((i,j, 0, area[i][j]))
#         while q:
#             x,y,t,virus = q.pop()
#             # area[x][y] = virus
#             if t >=s:
#                 continue
#             for dx, dy in dir:
#                 nx,ny = x+dx,y+dy
#                 if 0<=nx<n and 0<=ny<n:
#                     if visited[nx][ny] == -1:
#                         q.append((nx,ny,t+1,virus))
#                         visited[nx][ny] = t+1
#                         area[nx][ny] = virus
#                     elif visited[nx][ny] > t+1:
#                         q.append((nx,ny,t+1, virus))
#                         visited[nx][ny] = t+1
#                         area[nx][ny] = virus
#                     elif visited[nx][ny] == t+1 and area[nx][ny] > virus:
#                         q.append((nx,ny,t+1, virus))
#                         area[nx][ny] = virus
                        


# # print(area)
# # print(visited)

# print(tx,ty)
# # print(x,y)
# print(area[tx-1][ty-1])


# import sys
# input = sys.stdin.readline

# dir = [[1,0],[-1,0],[0,1],[0,-1]]
# n, k = map(int, input().split())
# area = []
# for _ in range(n):
#     area.append(list(map(int,input().split())))


# # virus = [[] for _ in range(k+1)]




# s,x,y = map(int, input().split())

# # for _ in range(s):
# #     newvirus = [[] for _ in range(k+1)]
# #     for i in range(len(virus)):
# #         for x, y in virus[i]:
# #             for di, dj in dir:
# #                 ni, nj = x + di, y + dj
# #                 if 0<=ni<n and 0<=nj<n and area[ni][nj] == 0:
# #                     newvirus[i].append((ni,nj))
# #                     area[ni][nj] = i
# #     for i in range(len(virus)):
# #         virus[i] += newvirus[i]


# visited = [[-1] *n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if area[i][j] != 0:
#             visited[i][j] = 0

# # for t in range(1,s+1):
# #     for i in range(n):
# #         for j in range(n):
# #             if area[i][j] != 0 and visited[i][j] == t-1:
# #                 for di, dj in dir:
# #                     ni, nj = i + di, j+dj
# #                     if 0<=ni<n and 0<=nj<n:
# #                         if visited[ni][nj] == -1:
# #                             area[ni][nj] = area[i][j]
# #                             visited[ni][nj] = t
                            
# #                         elif visited[ni][nj] == t:
# #                             if area[ni][nj] > area[i][j]:
# #                                 area[ni][nj] = area[i][j]

# #     # print(area)

# # # print(x,y)
# # print(area[x-1][y-1])


# import sys
# input = sys.stdin.readline

# dir = [[1,0],[-1,0],[0,1],[0,-1]]
# n, k = map(int, input().split())
# area = []
# for _ in range(n):
#     area.append(list(map(int,input().split())))


# virus = [[] for _ in range(k+1)]

# for i in range(n):
#     for j in range(n):
#         if area[i][j] != 0:
#             virus[area[i][j]].append((i,j))



# s,tx,ty = map(int, input().split())

# for _ in range(s):
#     newvirus = [[] for _ in range(k+1)]
#     for i in range(len(virus)):
#         for x, y in virus[i]:
#             for di, dj in dir:
#                 ni, nj = x + di, y + dj
#                 if 0<=ni<n and 0<=nj<n and area[ni][nj] == 0:
#                     newvirus[i].append((ni,nj))
#                     area[ni][nj] = i
#     virus = newvirus
# # print(area)
# # print(x,y)
# print(area[tx-1][ty-1])