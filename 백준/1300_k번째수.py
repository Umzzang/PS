import sys

n = int(input())
k = int(input())



l = 1
r = k
answer = 0
while l<=r:
    mid = (l+r)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n, mid//i)
    
    if cnt >= k:
        r = mid-1
        answer = mid
    else:
        l = mid+1

print(answer)


