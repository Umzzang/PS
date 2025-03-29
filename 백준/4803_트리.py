import sys

input = sys.stdin.readline
n, m = 1, 1
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a> b:
        parent[a] =b
    else:
        parent[b] = a

def check(i):
    cnt = 0
    # visited = [0] * (n+1)
    # visited[i] = 1
    # for j in graph[i]:
    #     if visited[j] == 0:
    #         cnt += 1 + check(j)
    # return cnt
    for j in range(1, len(parent)):
        
        if i == find(j):
            cnt += len(graph[j])
    return cnt



t = 1
while True:
    n, m = map(int, input().split())
    if n==0 and m ==0:
        break
    parent = [i for i in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        union(a,b)
        graph[a].append(b)
        # graph[b].append(a)
    
    tree = 0
    node = set()
    # print(graph)
    # print(parent)
    bridgecnt = {}  # 노드 개수
    nodecnt = {}    # 간선 개수
    for i in range(1, n+1):
        a = find(i)
        node.add(a)
        if bridgecnt.get(a):
            bridgecnt[a] += 1
        else:
            bridgecnt[a] = 1

    for i in node:
        nodecnt[i] = check(i)
        if bridgecnt[i] == nodecnt[i] + 1:
            tree += 1
        # print(nodecnt, bridgecnt)
        

   


    if tree == 1:
        print(f"Case {t}: There is one tree.")
    elif tree == 0:
        print(f"Case {t}: No trees.")
    else:
        print(f"Case {t}: A forest of {tree} trees.")
    t+=1
    

