import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n)]
# print(parent)
m = int(input())
# city = [[] for _ in range(n)]

# return 은 x 부모
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


## 뭐가 다른가
def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])

def union(i,j):
    i = find(i)
    j = find(j)
    if i != j:
        parent[max(i,j)] = min(i,j)


for i in range(n):
    c = list(map(int, input().split()))
    # city[i] = c
    for j in range(len(c)):
        if c[j] == 1:
            union(i,j)

travle = list(map(int, input().split()))


# union find
answer = "YES"
for i in range(1,len(travle)):
    if parent[travle[0]-1] != parent[travle[i]-1]:
        answer = "NO"
        break

print(answer)












# def bfs(s,e):
#     s-=1
#     e-=1
#     visited = [0] * (n+1)
#     visited[s] = 1
#     stack = [s]
#     while stack:
#         x = stack.pop()
#         # print(s,e,x)
#         if x == e:
#             return 0
#         for j in range(len(city[x])):
#             end = city[x][j]
#             # print(x,city[x], end)
#             if end == 1 and visited[j] == 0:
#                 stack.append(j)
#                 visited[j] = 1
#     return 1


# result = 1
# for i in range(len(travle)-1):
#     result = bfs(travle[i], travle[i+1])
#     if result:
#         break
    
# if result:
#     print("NO")
# else:
#     print("YES")




################################
# visited = [0] * n 
# def bfs(i):
#     stack = [i]
#     visited[i] = 1
#     while stack:
#         x = stack.pop()
#         for j in range(len(city[x])):
#             if city[x][j] == 1 and visited[j] == 0:
#                 stack.append(j)
#                 visited[j] = 1

# answer = "YES"
# bfs(travle[0]-1)
# for t in travle:
#     if visited[t-1] ==0:
#         answer = "NO"
#         break
# print(answer)

############################

