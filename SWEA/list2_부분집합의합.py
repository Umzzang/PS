t = int(input())

for test in range(1, t+1):
    n, k = map(int, input().split())
    cnt = 0
    a = [i for i in range(1, 13)]
    for i in range(1<<12):
        c = 0
        s = 0
        for j in range(12):
            if i & (1<<j):
                c += 1
                s += a[j]
        # if c == n and s == k:
        #     cnt += 1

            if c > n:
                break
        else:
            if c==n and s == k:
                cnt += 1
    
    print(f'#{test} {cnt}')