import math
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