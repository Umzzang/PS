import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))


start, end = 0, 0
t = arr[0]
l = 100001

while True:
    if t < s:
        end += 1
        if end >= n:
            break
        t += arr[end]
    else:
        l = min(l, end-start+1)
        t -= arr[start]
        start += 1

if l == 100001:
    print(0)
else:
    print(l)
        