import sys
input = sys.stdin.readline
t = int(input().rstrip())



for test in range(1, t+1):
    k, n, m = map(int, input().split(' '))
    abus = [0] * (n+1)
    bus = list(map(int , input().rstrip().split(' ')))
    for stop in bus:
        abus[stop] += k
    
    i = 0
    cnt = 0
    while i<n:
        
        for j in range(k, 0, -1):
            
            if i + j >= n:
                i = n
                break
            if abus[i+j] >0:
                i += j 
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{test} {cnt}')
    