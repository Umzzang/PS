n = int(input())

dp = [0] * (31)

dp[2] = 3
dp[4] = 11

for i in range(5, n+1):
    if i %2 == 0:
        dp[i] = 2 
        for j in range(0,i,2):
            if j == i-2:
                dp[i] += dp[j] *3
            else:
                dp[i] += dp[j] *2
    else:
        dp[i] = 0

print(dp[n])