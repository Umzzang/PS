import sys

input = sys.stdin.readline

n, m = map(int, input().split())
price = []
for _ in range(n):
    price.append(int(input()))


minp = min(price)
maxp = sum(price)

answer = maxp
def binary(l, r, count):
    global answer
    if l > r:
        return
    mid = (l+r)//2
    # print(mid, money(mid))
    if money(mid) > count or money(mid) == -1:
        binary(mid+1, r, count)
    else:
        answer = min(mid, answer)
        binary(l, mid-1, count)


    

def money(k):
    cnt = 1
    now = k
    if max(price) > k:
        return -1
    
    for i in range(n):
        if price[i] > now:
            cnt += 1
            now = k
            if price[i] > now:
                return -1
        
        now -= price[i]
    return cnt

binary(minp, maxp, m)
print(answer)
