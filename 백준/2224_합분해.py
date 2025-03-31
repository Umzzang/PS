n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]  #dp[i][j] 는 i를 만들기 위해 j개를 사용

for i in range(n+1):
    dp[i][1] = 1

for i in range(n+1):
    for j in range(2, k+1):
        
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

# for d in dp:
    # print(d)
print(dp[n][k] % 1000000000)
