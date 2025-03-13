import sys


input = sys.stdin.readline

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]
# result = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visited = [0] * (n+1)
stack = []
for i in range(1, n+1):
    if visited[i] == 0:
        stack.append(node[i])
        visited[i] = i
        while stack:
            x = stack.pop()
            for j in x:
                if visited[j] == 0:
                    stack.append(node[j])
                    visited[j] = i
# print(visited)
print(len(set(visited))-1)
                    