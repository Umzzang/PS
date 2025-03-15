import sys

input = sys.stdin.readline
n,m = map(int, input().split())
check = [0] * (n+1)
graph = [[] for _ in range(n+1)]
answer = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    check[b] += 1
q = []
for i in range(1, n+1):
    if check[i] == 0:
        q.append(i)

while q:
    node = q.pop()
    answer.append(node)
    for i in graph[node]:
        if check[i] == 1:
            q.append(i)
        check[i] -= 1

print(*answer)