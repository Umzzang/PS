import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
arr = [[] * v for _ in range(v+1)]
# print(arr)

maxv = 0

def bfs(i):
    global maxv
    renode = i
    visited = [0] * (v+1)
    
    visited[i] = 1
    stack = deque()
    
    stack.append((i, 0))
        
    while stack:
        
        node, dis = stack.pop()
        
        
        
        for nnode, ndis in arr[node]:
            if visited[nnode] == 0:
                stack.append((nnode, ndis+dis))
                visited[nnode] = 1
                if dis+ndis > maxv:
                    maxv = dis + ndis
                    renode = nnode
                        
    return renode, maxv


for i in range(1, v+1):
    vdata = list(map(int, input().split()))
    
    for j in range(1, len(vdata)-1, 2):
        
        arr[vdata[0]].append((vdata[j], vdata[j+1]))

node, dis = bfs(1)
node, dis = bfs(node)

print(dis)
