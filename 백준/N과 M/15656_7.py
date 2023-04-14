import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))
arr.sort()
answer = []

def bfs(i):
    if i > m:
        print(*answer)
        return
    for j in range(1, n+1):
        answer.append(arr[j])
        bfs(i+1)
        answer.pop()

bfs(1)