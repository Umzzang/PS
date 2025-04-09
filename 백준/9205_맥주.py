import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def distance(i,j,di,dj):
    if abs(di-i) + abs(dj -j) <= 1000:
        return True
    return False

for _ in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    
    rock = list(map(int, input().split()))
    store = [house] + store
    visited = [0] * (n + 1)
    si, sj = house
    ei, ej = rock
    possible = 0
    q= deque()
    q.append(0)
    # for i in range(len(store)):
    #     ni,nj = store[i]
    #     if distance(si, sj, ni,nj):
    #         q.append(i)
    #         visited[i] = 1


    while q:
        x = q.popleft()
        ni ,nj = store[x]
        if distance(ni, nj, ei, ej):
            possible = 1
            print("happy")
            break
        for i in range(1, len(store)):
            if visited[i] == 0 and distance(ni,nj, store[i][0], store[i][1]):
                q.append(i)
                visited[i] = 1
    
    if possible == 0:
        print("sad")







        # for ni,nj in store:
        #     if distance(si, sj, ni,nj):
        #         si, sj = ni, nj
        #         continue
        #     else:
        #         possible = 0
        #         print("sad")
        #         break
        # if possible == 0:
        #     break
        # if distance(si, sj, ei, ej):
        #     print("happy")
        #     break
        # else:
        #     print("sad")
        #     break