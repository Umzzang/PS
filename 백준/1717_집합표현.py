import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = {}

def union(a,b):
    a = find2(a)
    b = find2(b)

    if a != b:
        parent[min(a,b)] = max(a,b) 

def find(x):
    if x != parent[x]:
        x = find(parent[x])
    return x

def find2(x):
    if parent[x] != x:
        parent[x] = find2(parent[x])
    return parent[x]

for _ in range(m):
    c, a, b =  map(int, input().split())
    if parent.get(a) is None:
        parent[a] = a
    if parent.get(b) is None:
        parent[b] = b

    
    if c == 1:
        if find2(a) == find2(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)
print(parent)