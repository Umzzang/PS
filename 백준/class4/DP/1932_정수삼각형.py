import sys
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n)]
dp = [] 
for i in range(n):
    # print(dp)
    nlst = list(map(int, input().split()))
    if len(nlst) == 1:
        dp = [nlst[0]]
    elif len(nlst) == 2:
        dp = [dp[0] + nlst[0], dp[0] + nlst[1]]
    else: 
        dp2 = dp[:]
        end = dp2[-1]     
        for j in range(len(nlst)-1):
            if j == 0:
                dp[j] = dp2[j] + nlst[j]
            else:
                dp[j] = max(dp2[j] + nlst[j], dp2[j-1] +nlst[j])
        dp = dp + [end + nlst[-1]]

print(max(dp))