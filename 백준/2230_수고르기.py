import sys

input = sys.stdin.readline

n, m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
answer = arr[-1] - arr[0]

l = 0
r = 0
while r <= n-1:

    res = arr[r] - arr[l]
    if res == m:
        answer = m
        break
    elif res > m:
        if res < answer:
            answer = res
        l += 1
    else:
        r += 1

print(answer)