import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 1000000000
arr = [[inf] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 0

for _ in range(m):
    s, e, c = map(int, input().split())
    if arr[s][e] < c:
        continue
    else:
        arr[s][e] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            for k in range(1, n+1):
                if k != j:
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for i in range(n+1):
    for j in range(n+1):
        if arr[i][j] == inf:
            arr[i][j] = 0

for i in range(1, n+1):
    print(*arr[i][1:])
