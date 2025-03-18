import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int, input().split())

bridges = [[] for _ in range(n)]


maxg = 0
ming = 1000000001
parent = [i for i in range(n)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(i, j):
    i = find(i)
    j = find(j)
    if i<j:
        parent[j] = i
    else:
        parent[i] = j

for _ in range(m):
    a,b,c = map(int, input().split())
    bridges[a-1].append((b-1, c))
    bridges[b-1].append((a-1, c))
    maxg = max(maxg, c)
    ming = min(ming, c)
    union(a-1,b-1)
# print(bridges)
s, e = map(int, input().split())
answer = 0




# def dfs(start, w):
#     global answer
#     if start == e-1:
#         # print(1)
#         answer = max(answer, w)
    
#     if w < answer:
#         return

#     for land, weight in bridges[start]:
#         if parent[land] == parent[e-1] and visited[land] == 0:
#             if weight<w:
#                 visited[land] = 1
#                 dfs(land, weight)
#                 visited[land] = 0
#             else:
#                 visited[land] = 1
#                 dfs(land, w)
#                 visited[land] = 0

# print("brideges", bridges)
def bfs(start, weight):
    # maxweight = sys.maxsize
    visited = [0] * n
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        # print("q", q)
        x = q.popleft()
        if x == e-1:
            return True
        for land, w in bridges[x]:
            if visited[land] ==0 and w >= weight:
                q.append(land)
                visited[land] = 1
                # maxweight = m+in(maxweight, w)

answer = 0
while ming <= maxg:
    midg = (ming + maxg) // 2
    # print(ming, maxg, midg)
    # print(bfs(s-1, midg))
    
    if bfs(s-1, midg):
        answer = midg
        ming = midg +1
    else:
        maxg = midg -1


print(answer)