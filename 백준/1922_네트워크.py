import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
nets = [[] for i in range(n+1)]
cost = 0
for _ in range(m):
    # net.append(list(map(int, input().split())))
    s, e, c = map(int, input().split())
    nets[s].append((c,e))
    nets[e].append((c, s)) 



def search(x):
    global cost
    edge = [x]
    visited = [0] * (n+1)
    # visited[x] = 1
    tmp = []

    while len(edge) < n:
        if visited[x] == 0:
            for net in nets[x]:
                heapq.heappush(tmp, net)
            visited[x] = 1
        
        
        co, end = heapq.heappop(tmp)
        if end not in edge:
            cost += co
            edge.append(end)
            x = end
        # print(edge)
        

    

search(1)
print(cost)





# net.sort(key=lambda x : x[2])
# parent = [i for i in range(n+1)]
# def find(x):
#     if x == parent[x]:
#         return parent[x]
#     parent[x] = find(parent[x])
#     return parent[x]

# def union(x,y):
#     x = find(x)
#     y = find(y)

#     if x> y:
#         parent[x] = y
#     elif x< y:
#         parent[y] = x


# for n in net:
#     s,e,c = n
#     if find(s) == find(e):
#         continue
#     else:
#         cost += c
#         # print(s,e,c)
#         union(s,e)

# # print(parent)
# print(cost)

