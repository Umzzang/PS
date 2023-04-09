import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

maxV = 0

for i in range(n):
    v = lcs(i)
    if maxV < v:
        maxV = v

print(maxV)


def lcs(i):
    increase = []
    decrease = []
    
    pass



