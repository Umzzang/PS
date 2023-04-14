import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()
answer = [0] * m

vis = [0] * n

def bfs(i):
    if i > m:
        print(*answer)
        return
    tmp = 0
    for j in range(n):
        if vis[j] == 0 and tmp != arr[j]:
            answer[i-1] = arr[j]
            tmp = arr[j]
            vis[j] = 1
            bfs(i+1)
            vis[j] = 0



bfs(1)

# 처음에 bfs 안에 visited * 10001 로 체크했는데 그럴 필요 없음;;
