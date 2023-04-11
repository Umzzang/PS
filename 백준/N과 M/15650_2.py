n, m = map(int,input().split())

arr = []
visited = [0] * (n+1)

def dfs(start):
    if m == len(arr):
        print(*arr)
        return
    for j in range(start, n+1):
        if visited[j] == 1:
            continue
        arr.append(j)
        visited[j] = 1
        dfs(j+1)
        arr.pop()
        visited[j] = 0

    
dfs(1)