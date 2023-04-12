import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
answer = [0] * m


def bfs(i):
    if i > m:
        print(*answer)
        return
    tmp = 0
    for j in range(n):
        if tmp != arr[j]:
            answer[i-1] = arr[j]
            tmp = arr[j]
            bfs(i+1)

bfs(1)