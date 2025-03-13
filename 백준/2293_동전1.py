import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
answer = [0] * (k+1)

for _ in range(n):
    coin.append(int(input()))

answer[0] = 1
for c in coin:
    for i in range(c, k+1):
        answer[i] = answer[i] + answer[i-c]

print(answer[-1])