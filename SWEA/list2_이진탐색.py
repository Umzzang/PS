t = int(input())
def bs(sp, lp, ssp, cnt):
    mid = int((sp+lp)/2)
    if mid == ssp:
        return cnt
    elif ssp > mid:
        return bs(mid, lp, ssp, cnt+1)
    else:
        return bs(sp, mid, ssp, cnt+1)

for tc in range(1, t+1):
    p, a, b = map(int, input().split())
    at = bs(1, p, a, 1)
    bt = bs(1, p, b, 1)
    if at == bt:
        print(f'#{tc} 0')
    elif at > bt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} A')
    