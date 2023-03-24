t = int(input())
for test in range(1, t+1):
    n, m = map(int, input().split(' '))
    l = list(map(int, input().split(' ')))
    base = 0
    for i in range(m):
        base += l[i]

    maxx, minn = base, base
    for i in range(n-m+1):
        s = 0
        for j in range(m):
            s += l[i+j]
        if s > maxx:
            maxx = s
        if s < minn:
            minn = s
    print(f'#{test} {maxx - minn}')