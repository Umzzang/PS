import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(start):
   
    # possible = []
    next = student[start]
    # print(visited)
    if visited[start] == 2: 
        return 
    if visited[start] == -1:
        return
    
    visited[start] += 1
    if visited[next] != -1:
        find(next)
    if visited[start] == 1:
        visited[start] = -1
    
    

    
     

tc= int(input())
for _ in range(tc):
    n = int(input())
    student = [0] + list(map(int ,input().split()))
    visited = [0] * (n+1) # 0 이면 미방문, 1이면 가능, 2면 탐색중?
    for i in range(1, n+1):
        if visited[i] == 0 :
            find(i)
    cnt = 0
    for i in range(1, n+1):
        if visited[i] == 2:
            cnt += 1

    print(n-cnt)