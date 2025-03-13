import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
number.sort()
cnt = 0
def binary(l, r, target,ni):
    start = number[l]
    end = number[r]
    if l == r:
        return 0
    if start + end == target:
        if l == ni:
            return binary(l+1, r, target, ni)
        elif r == ni:
            return binary(l, r-1, target, ni)
        else:
            return 1
    elif start + end < target:
        return binary(l+1, r, target, ni)
    else:
        return binary(l, r-1,target, ni)
    
for i in range(n):
    cnt += binary(0, n-1, number[i], i)

print(cnt)