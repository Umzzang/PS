import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for a in arr:
    if dp[-1] < a:
        dp.append(a)
    else:
        start = 0
        end = len(dp)
        while start < end:
            mid = (start + end) // 2
            if dp[mid] > a:
                end = mid 
            else:
                
                start = mid + 1

        dp[end] = a

print(len(dp) -1)