import sys
input = sys.stdin.readline


def find(x):
    global parent
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    global parent
    x = find(x)
    y = find(y)
    if x> y:
        parent[x] = y
    elif x<y:
        parent[y] = x

n  = int(input())
island = [[]  for _ in range(n+1)]

parent = [i for i in range(n+1)]
for _ in range(n-2):
    a, b = map(int, input().split())
    # island[a].append(b)
    # island[b].append(a)
    union(a,b)

# for i in range(1, len(island)):
#     for j in island[i]:
#         union(i,j)

answer = parent[1]
for i in range(2, n+1):
    if find(1) != find(i):
        answer = i
        break
    if parent[i] != answer:
        answer = i
        break
# print(parent)
print(1, answer)