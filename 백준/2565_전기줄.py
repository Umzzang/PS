import sys
input = sys.stdin.readline

n = int(input())
ele = []
for _ in range(n):
    a, b= map(int, input().split())
    ele.append((a,b))

ele.sort()
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if ele[j][1] < ele[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
