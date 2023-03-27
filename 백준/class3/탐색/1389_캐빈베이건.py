# 그래프, 플로이드-워샬

import sys
import math
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [[math.inf] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arr[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            for k in range(1, n+1):
                if k != i and k != j:
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])


p = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, n+1):
        p[i] += arr[i][j]


maxV = math.inf
idx = 0
for i in range(n, 0, -1):
    if p[i] <= maxV:
        idx = i
        maxV = p[i]

print(idx)