import sys

input = sys.stdin.readline


n = int(input())

x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])
sx = 0
sy = 0

for i in range(n):
    sx += x[i] * y[i+1]
    sy += y[i] * x[i+1]

print(round(abs((sx-sy)/2),1))