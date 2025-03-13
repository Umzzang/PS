import sys

input =  sys.stdin.readline

fstring = input().rstrip()
sstring = input().rstrip()

n = len(fstring)
m = len(sstring)

dp = [[0] * (m+1) for _ in range(n+1)]  #dp[i][j] 는 

for i in range(n):
    for j in range(m):
        if fstring[i] == sstring[j]:
            # print(1)
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
# print(dp)
print(dp[-1][-1])