import sys
input = sys.stdin.readline
n= int(input())
arr = list(map(int, input().split()))

dp = [1] * n
# dp[0] = 1
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        # else:
        #     dp[i] = max(dp[j], dp[i])

l = max(dp)
print(l)
answer = []

for i in range(n-1, -1, -1):
    if dp[i] == l:
        answer.append(arr[i])
        l -= 1


print(*sorted(answer))