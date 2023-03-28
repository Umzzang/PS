t = int(input())

def get_gdc(a, b):
    if b == 0:
        return a
    return get_gdc(b, a%b)


for tc in range(1, t+1):
    m, n, x, y = map(int, input().split())
    # print(83%13, 83%11)
    gdc = get_gdc(m, n)
    g = m*n//gdc
    while x <= g:
        cnt = x
        if x % n == y % n:
            print(x)
            break
        else:
            x += m
    if x > g:
        print(-1)