import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
def d(n):
    return (n*2)%10000

def s(n):
    if n == 0:
        return 9999
    else:
        return n-1
    

def l(n):
    n = str(n)
    n = n.zfill(4)
    n = n[1:] + n[0]
    return int(n)

def r(n):
    n = str(n)
    n = n.zfill(4)
    n = n[-1] + n[:-1]
    return int(n)
# print(r(1))

def dslr(nlst):
    new_nlst = []
    for n in nlst:
    
        dn = d(n)
        sn = s(n)
        ln = l(n)
        rn = r(n)
        if visited[dn] == 0:
            visited[dn] = visited[n] + 'D'
            new_nlst.append(dn)
        if visited[sn] == 0:
            visited[sn] = visited[n] + 'S'
            new_nlst.append(sn)
        if visited[ln] == 0:
            visited[ln] = visited[n] + 'L'
            new_nlst.append(ln)
        if visited[rn] == 0:
            visited[rn] = visited[n] + 'R'
            new_nlst.append(rn)

    return new_nlst




for _ in range(t):
    visited = [0] * 10000   
    a, b = map(int, input().split())
    nlst = deque()
    nlst.append(a)
    
    visited[a] = ''

    # while True:
    #     nlst = dslr(nlst)
    #     if visited[b] != 0:
    #         break
    while nlst:
        # print(nlst)
        n = nlst.popleft()
        # print(n, visited[1000])
        if visited[b] != 0:
            break
        else:
            dn = d(n)
            sn = s(n)
            ln = l(n)
            rn = r(n)
            # print(dn, sn, ln, rn)
            # print(visited[dn], visited[sn], visited[ln], visited[rn])
            if visited[dn] == 0:
                visited[dn] = visited[n] + 'D'
                nlst.append(dn)
            if visited[sn] == 0:
                visited[sn] = visited[n] + 'S'
                nlst.append(sn)
            if visited[ln] == 0:
                visited[ln] = visited[n] + 'L'
                nlst.append(ln)
            # print(visited[1000])
            if visited[rn] == 0:
                visited[rn] = visited[n] + 'R'
                nlst.append(rn)

    

    print(visited[b])
    