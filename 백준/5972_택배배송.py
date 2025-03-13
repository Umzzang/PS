import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

mlst = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    mlst[s].append((c, e))
    mlst[e].append((c, s))

def dik(start):
    # visitied = [0] * (n+1)
    q = [(0, start)]
    d = [sys.maxsize] * (n+1)
    d[start] = 0
    while q:
        _, x = heapq.heappop(q)
        # if visitied[x]:
        #     continue
        # visitied[x] = 1
        for cost, end in mlst[x]:
            if d[end] > cost + d[x]:
                d[end] = cost + d[x]
                heapq.heappush(q, (cost, end))
    return d
d = dik(1)
print(d[n])