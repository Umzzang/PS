import sys

input = sys.stdin.readline

n = int(input())

def mul(f, arr2):
    return f * arr2[0] * arr2[1]

lst = []
dp = [0] * n
for _ in range(n):
    lst.append(list(map(int,input().split())))
first = lst[0][0]
last = lst[n-1][1]
for i in range(1, n):
    dp[i] = dp[i-1] + mul(first, lst[i])

for i in range(n-1, 0, -1):
    dp[i] = min(dp[i], dp[i-1] + mul(last, lst[i-1]))

print(dp)





