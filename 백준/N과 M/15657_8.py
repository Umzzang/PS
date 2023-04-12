import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

arr.sort()

answer = [0] * m

def bfs(i, start):
    if i > m:
        print(*answer)
        return
    for j in range(start, n+1):
        answer[i-1] = arr[j]
        bfs(i+1, j)    

bfs(1, 1)
