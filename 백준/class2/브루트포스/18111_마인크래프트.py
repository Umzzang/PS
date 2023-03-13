import sys
inpu = sys.stdin.readline

n, m, b = map(int, inpu().split(' '))
area = []
minx = 256
maxx = 0
for _ in range(n):
    a = list(map(int, inpu().split(' ')))
    if min(a) < minx:
        minx = min(a)
    if max(a) > maxx:
        maxx = max(a)
    area.append(a)

ans = 257 * 257 * 500 * 2
h = -1

for t in range(minx, maxx+1):
    take = 0
    use = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] > t:
                take += area[i][j] - t
            else:
                use += t - area[i][j]

    if b + take < use:
        continue

    if ans >= take * 2 + use:
        ans = take * 2 + use
        h = t

print(ans, h)



