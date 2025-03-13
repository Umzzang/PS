import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
alst = list(map(int, input().split()))
m = int(input())
blst = list(map(int, input().split()))

possiblea = {}
possibleb = {}

bigger = max(n, m)

for i in range(n):
    s = alst[i]
    if possiblea.get(s):
            possiblea[s] += 1
    else:
        possiblea[s] = 1
    for j in range(i+1, n):
        s += alst[j]
        if possiblea.get(s):
            possiblea[s] += 1
        else:
            possiblea[s] = 1

for i in range(m):
    s = blst[i]
    if possibleb.get(s):
            possibleb[s] += 1
    else:
        possibleb[s] = 1
    for j in range(i+1, m):
        s += blst[j]
        if possibleb.get(s):
            possibleb[s] += 1
        else:
            possibleb[s] = 1


answer = 0
for i in possiblea.keys():
    target = t - i
    if possibleb.get(target):
        answer += possiblea[i] * possibleb[target]

print(answer)
