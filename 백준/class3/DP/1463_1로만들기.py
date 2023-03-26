n = int(input())
# 이렇게 하면 n 2이하일때 인덱스 에러나옴
# dp = [0] * (n+1)
# dp[0] = 0
# dp[1] = 0
# dp[2] = 1

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 0


for i in range(2, n+1):
    
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)




# print(dp)


# 첫번째 풀이
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 0


for i in range(2, n+1):
    
    if i % 3 == 0:
        k = dp[i//3] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, k)
        else:
            dp[i] = min(k, dp[i-1] + 1)
    elif i % 3 == 1:
        k = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, k)
        else:
            dp[i] = min(k, dp[i-1] + 1)
    else:
        k = dp[i-2] + 2
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, k)
        else:
            dp[i] = min(k, dp[i-1] + 1)




print(dp[n])