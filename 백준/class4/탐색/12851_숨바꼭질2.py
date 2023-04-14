from collections import deque
n, k = map(int, input().split())

visited = [100000] * (100001)
visited[n] = 0
cnt = 0

q = deque()
q.append(n)
time = 100000
while q:
    # print(q)
    # print(visited[k])
    now = q.popleft()
    if visited[now] > time:
        continue

    if now == k:
        if time > visited[k]:
            time = visited[k]
            cnt = 1
        elif time == visited[k]:
            cnt += 1
        continue

     


    bn = now - 1
    an = now + 1
    jn = now * 2
    if 0<=bn<=100000 and visited[bn] >= visited[now] + 1:
        q.append(bn)
        visited[bn] = visited[now] + 1
    if 0<=an<=100000 and visited[an] >= visited[now] + 1:
        q.append(an)
        visited[an] = visited[now] + 1
    if 0<=jn<=100000 and visited[jn] >= visited[now] + 1:
        q.append(jn)
        visited[jn] = visited[now] + 1
    


print(time)
print(cnt)