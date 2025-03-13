import sys
imput = sys.stdin.readline

n, r, c = map(int, input().rstrip().split())
cnt = 0
answer = 0
def f(n, i, j):
    
    global cnt, answer
    if answer == 1:
        return
    if r<i or r>=i+n or c<j or c>=j+n:
        cnt += n ** 2
        return
    if n > 2:
        n //= 2
        f(n, i, j)
        f(n, i, j+n)
        f(n, i+n, j)
        f(n, i+n, j+n)
    else:
        answer = 1
        if i == r:
            if j == c:
                cnt += 0
            else:
                cnt += 1
        else:
            if j == c:
                cnt += 2
            else:
                cnt += 3
        return
        
        
            

f(2**n, 0, 0)
print(cnt)