n, m = map(int, input().split())
base = [[0] * n for _ in range(m)]

front = [] # n
right = [] # m
for _ in range(n):
    front.append(int(input()))

for _ in range(m):
    right.append(int(input()))


