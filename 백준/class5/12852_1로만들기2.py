from collections import deque
n = int(input())

visited = [n+1] * (n+1)

visited[1] = 0



q = deque()
q.append((1, [1]))
result = []
while q:
    i, p = q.popleft()
    
    if i == n:
        result = p
        break

    mi = i * 2
    ti = i * 3
    pi = i + 1
    if mi <= n and visited[mi] > visited[i] + 1:
        q.append((mi, [mi] + p))
        visited[mi] = visited[i] + 1      
    if ti <= n and visited[ti] > visited[i] + 1:
        q.append((ti, [ti] + p))
        visited[ti] = visited[i] + 1     
    if pi <= n and visited[pi] > visited[i] + 1:
        q.append((pi, [pi] + p))
        visited[pi] = visited[i] + 1     

print(visited[n])
print(*result)
