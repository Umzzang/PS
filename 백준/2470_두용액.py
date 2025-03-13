import sys

input = sys.stdin.readline

n = int(input())
liq = list(map(int,input().split()))
liq.sort()

l = 0
r = n-1
answer = liq[0] + liq[n-1]
final = [liq[0], liq[n-1]]

while l < r:
    sum = liq[l] + liq[r]
    if abs(sum) < abs(answer):
        answer = abs(sum)
        final = [liq[l], liq[r]]
    if sum > 0 :
        r -= 1
    elif sum < 0:
        l += 1
    else:
        break

print(*final)