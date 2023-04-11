n, m = map(int,input().split())
arr = []
visited = [0] * (n+1)
def dfs():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        else:
            arr.append(i)
            visited[i] = 1
            dfs()
            arr.pop()
            visited[i] = 0
    
dfs()