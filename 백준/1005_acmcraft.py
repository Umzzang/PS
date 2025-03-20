import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    times = [0]+ list(map(int, input().split()))
    dp = times[:]
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    graph2 = [[] for _ in range(n+1)]
    ingred = [0] * (n+1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph2[y].append(x)
        graph[x].append(y)
        ingred[y] += 1

    topology = []
    q = []
    for i in range(1, len(ingred)):
        if ingred[i] == 0:
            q.append(i)

    while q:
        x = q.pop(0)
        topology.append(x)
        for child in graph[x]:
            ingred[child] -= 1
            if ingred[child] == 0:
                q.append(child)

    for tmp in topology:
        if graph2[tmp]:
            for t in graph2[tmp]:
                dp[tmp] = max(dp[tmp], dp[t] + times[tmp])





    target = int(input())
    print(dp[target])







    # def search(t):
    #     # visited[t] = 1
    #     for p in graph[t]:
    #         # if not visited[p]:
    #         search(p)
    #         dp[t] = max(times[t] + dp[p], dp[t])
    #         # visited[t] = 1 

    # # print(graph)
    # search(target)
    # print(dp)
    # print(dp[target])