import sys
from collections import deque

input = sys.stdin.readline


def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    parent = [0 for _ in range(n + 1)]
    check = [0 for _ in range(n + 1)]

    q = deque()
    q.append(1)
    while q:
        tmp = q.popleft()
        check[tmp] = 1
        tmplist = graph[tmp]
        for t in tmplist:
            if check[t] == 0:
                parent[t] = tmp
                q.append(t)

    for i in range(2, n + 1):
        print(parent[i])


if __name__ == "__main__":
    main()
