import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

ans = ''


def s(n, i, j):
    global ans
    
    fir = arr[i][j]
    flag = 0
    for x in range(n):
        for y in range(n):
            if arr[i+x][j+y] != fir:
                n //= 2
                ans += '('
                s(n, i, j)
                s(n, i, j+n)
                s(n, i+n, j)
                s(n, i+n, j+n)
                flag = 1
                ans += ')'
                break
        if flag == 1:
            break
    else:
        if n > 1:
            ans += str(fir) 
        else:
            ans += str(fir)
        
    


s(n, 0, 0)
print(ans)