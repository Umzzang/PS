import sys

input = sys.stdin.readline

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

def dfsh(max, min):
    answer = 0
    for i in range(min-1, max+1):
        if answer < dfs(i):
            answer = dfs(i)
    return answer

def dfs(h):
    visited = [[0] * n for _ in range(n)]
    stack = []
    count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and visited[i][j] == 0:
                stack.append([i,j])
                visited[i][j] = 1
                count += 1
                while stack:
                    x, y = stack.pop()
                    if x >0 and area[x-1][y] > h and visited[x-1][y] == 0:
                        stack.append([x-1, y])
                        visited[x-1][y] = 1
                    if x < n-1 and area[x+1][y] > h and visited[x+1][y] == 0:
                        stack.append([x+1, y])
                        visited[x+1][y] = 1
                    if y > 0 and area[x][y-1] > h and visited[x][y-1] == 0:
                        stack.append([x, y-1])  
                        visited[x][y-1] = 1
                    if y < n-1 and area[x][y+1] > h and visited[x][y+1] == 0:
                        stack.append([x, y+1])
                        visited[x][y+1] = 1
    return count
                    


    


maxh = 0
minh = 101
for i in range(n):
    for j in range(n):
        if area[i][j] > maxh:
            maxh = area[i][j]
        if area[i][j] < minh:
            minh = area[i][j]

print(dfsh(maxh, minh))