import sys

input = sys.stdin.readline

n = int(input())



dp = list(map(int, input().split()))

dp2 = dp[:]

for _ in range(n-1):
    now = list(map(int, input().split()))
    dp3 = dp[:]
    dp4 = dp2[:]
    
    for i in range(3):
        if i == 0:
            dp[i] = max(now[i] + dp3[i], now[i] + dp3[i+1])
            dp2[i] = min(now[i] + dp4[i], now[i] + dp4[i+1])
        elif i == 2:
            dp[i] = max(now[i] + dp3[i], now[i] + dp3[i-1])
            dp2[i] = min(now[i] + dp4[i], now[i] + dp4[i-1])
        else:
            dp[i] = max(now[i] + dp3[i], now[i] + dp3[i-1], now[i] + dp3[i+1])
            dp2[i] = min(now[i] + dp4[i], now[i] + dp4[i-1], now[i] + dp4[i+1])

print(max(dp), min(dp2))