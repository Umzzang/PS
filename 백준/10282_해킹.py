import sys
import heapq

input = sys.stdin.readline

t = int(input())

def dijck(start):
    seen = set()
    
    visited = [sys.maxsize] * (n+1)
    visited[start] = 0
    temp = [(0, start)]
    time = []
    while temp:
        _, now = heapq.heappop(temp)
        if now in seen:
            continue
        seen.add(now)
        for next, cost in graph[now]:
            if visited[next] > visited[now] + cost:
                visited[next] = visited[now] + cost
                heapq.heappush(temp, (visited[next], next))
    maxtime = 0
    for i in seen:
        maxtime = max(visited[i], maxtime)

    return len(seen), maxtime





for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[]  for _ in range(n+1)]
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        # graph[a].append((b, s))
        graph[b].append((a, s))

    a, b = dijck(c)
    print(a, b)