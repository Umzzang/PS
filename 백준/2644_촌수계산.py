from sys import stdin

input = stdin.readline


def find(a,b):
    answer  = -1
    
    visited = [0] * (n+1)
    stack = [(a,0)]
    while stack:
        
        x, count = stack.pop()
        visited[x] = 1
        for i in parent[x]:
            if i == b:
                return count+1
            else:
                if visited[i] == 0:
                    stack.append((i, count+1))


    return answer
    


n = int(input())

a, b = map(int, input().split())
parent = [[] for _ in range(n+1)]

m = int(input())
for _ in range(m):
    p, c = map(int, input().split())
    parent[c].append(p)
    parent[p].append(c)
# print(parent)
print(find(a,b))