import sys
from collections import deque
sys.setrecursionlimit(10**7)

f, s, g,u,d = map(int ,input().split())

visited = [-1] * (f+1)

visited[s] = 0

# def move(now, ud, stairs, cnt):
#     if ud == 0 : # 아래
#         if now - stairs < 1:
#             return
#         else:
#             if visited[now - stairs] == -1:
#                 visited[now - stairs] = cnt
#                 move(now-stairs, 0, d, cnt+1)
#                 move(now-stairs, 1, u, cnt+1)
#             elif visited[now-stairs] <= cnt:
#                 return
#             else:
#                 visited[now-stairs] = cnt
#                 move(now-stairs, 0, d, cnt+1)
#                 move(now-stairs, 1, u, cnt+1)
#     else: # 위
#         if now + stairs > f:
#             return
#         else:
#             if visited[now+stairs] == -1:
#                 visited[now+stairs] = cnt
#                 move(now+stairs, 0, d, cnt+1)
#                 move(now+stairs, 1, u, cnt+1)
#             elif visited[now + stairs] <= cnt:
#                 return
#             else:
#                 visited[now + stairs] = cnt
#                 move(now+stairs, 0, d, cnt+1)
#                 move(now+stairs, 1, u, cnt+1)


# move(s, 0, d, 1)
# move(s, 1, u, 1)

answer = -1
def bfs(start):
    global answer
    q = deque()
    q.append((start, 0))
    visited[start] = 0
    while q:
        x, cnt = q.popleft()
        if x == g:
            answer = cnt
            return
        if x + u <=f and (visited[x+u] == -1 or visited[x+u] > cnt + 1):
            q.append((x+u, cnt+1))
            visited[x+u] = cnt+1
        if x - d >= 1 and  (visited[x-d] == -1 or visited[x-d] > cnt + 1):
            q.append((x-d, cnt+1))
            visited[x-d] = cnt+1


bfs(s)



if answer == -1:
    print('use the stairs')
else:
    print(answer)