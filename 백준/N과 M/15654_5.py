import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

arr.sort()
visited = [0] * (n+1)
answer = []
def bfs(i):
    if i > m:
        print(*answer)
        return
    for j in range(1, n+1):
        if visited[j] == 0:
            answer.append(arr[j])
            visited[j] = 1
            bfs(i+1)
            answer.pop()
            visited[j] = 0


bfs(1)