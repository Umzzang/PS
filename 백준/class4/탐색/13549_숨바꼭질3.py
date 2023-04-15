from collections import deque

n, k = map(int, input().split())

visited = [100001] * 100001
q = deque()
q.append(n)
time = 1000000
visited[n] = 0
while q:
    
    now = q.popleft()
    # print(now)
    if visited[now] > time:
        continue
    if now == k and time > visited[k]:
        time = visited[k]
        continue
    bq = now - 1
    aq = now + 1
    jq = now * 2
    if 0<=jq<=100000 and visited[jq] > visited[now]:
        q.append(jq)
        visited[jq] = visited[now]
    if 0<=bq<=100000 and visited[bq] > visited[now] + 1:
        q.append(bq)
        visited[bq] = visited[now] + 1
    if 0<=aq<=100000 and visited[aq] > visited[now] + 1:
        q.append(aq)
        visited[aq] = visited[now] + 1


print(time)

### 0-1 bfs
### 0의 가중치를 q맨 앞으로 넣는 방식
from collections import deque

n, k = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
q = deque()
q.append(n) 
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(visited[s])
        break
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        visited[s-1] = visited[s] + 1
        q.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        q.appendleft(s*2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        q.append(s+1)