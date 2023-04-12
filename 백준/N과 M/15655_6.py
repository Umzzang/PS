n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

arr.sort()

answer = []

def bfs(i, start):
    if i > m:
        print(*answer)
        return
    
    for j in range(start, n+1):
        answer.append(arr[j])
        bfs(i+1, j+1)
        answer.pop()


bfs(1, 1)