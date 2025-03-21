n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [[0,0] for _ in range(n)] # 0 은 마지막 1은 한번 더 남음
dp[0][0] = 0
dp[0][1] = stairs[0]
if n > 1:
    dp[1][0] = stairs[0] + stairs[1]
    dp[1][1] = stairs[1]

    for i in range(2, n):
        dp[i][0] = dp[i-1][1] + stairs[i]
        dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
    # print(dp)
print(max(dp[n-1][0], dp[n-1][1]))
