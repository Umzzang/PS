import sys
input = sys.stdin.readline

n = int(input())

liq = list(map(int, input().split()))

liq.sort()

target = [liq[0], liq[1], liq[2]]
answer = sum(target)

def binary(x):
    global answer
    global target
    l = x+1
    r = n-1
    while l<r:
        sum = liq[x] + liq[l] + liq[r]
        if abs(sum) < abs(answer):
            target = [liq[x], liq[l], liq[r]]
            answer = sum
            if answer == 0:
                return 1
        
        if sum > 0:
            r -=1
        else:
            l += 1



for i in range(n-2):
    if binary(i) == 1:
        break
print(*target)