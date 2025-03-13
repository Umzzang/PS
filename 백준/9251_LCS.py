import sys

input =  sys.stdin.readline

fstring = input().rstrip()
sstring = input().rstrip()

n = len(fstring)
m = len(sstring)

dp = [[0] * (n+1) for _ in range(m+1)]  #dp[i][j] 는 

for i in range(1,n+1):
    for j in range(1,m+1):
        if fstring[i-1] == sstring[j-1]:
            # print(1)
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# print(dp)
print(dp[-1][-1])