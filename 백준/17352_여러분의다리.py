import sys
input = sys.stdin.readline


def find(x):   #  1 2 3 4
    # global parent
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    # global parent
    x = find(x)
    y = find(y)
    if x> y:
        parent[x] = y
    elif x<y:
        parent[y] = x

n  = int(input())
island = [[]  for _ in range(n+1)]

parent = [i for i in range(n+1)]    # 
for _ in range(n-2):
    a, b = map(int, input().split())
    union(a,b)

print(parent)
answer = parent[1]
for i in range(2, n+1):
    # if find(1) != find(i):
    #     answer = i
    #     break
    if parent[i] != parent[1]:  ###### parent가 무조건 부모를 가르키지않네??? 입력순서에따라
        print(1, i)
        break

# print(1, answer)