from collections import deque
n,k=map(int,input().split())
area = [[] for _ in range(100001)]



visited = [-1] * 100001

path = [0] * 100001

def move(i, t):
    q = deque()
    q.append(i)
    visited[i] = i
    
    while q:
        x = q.popleft()
        # time = len(path) - 1
        # print(x, q)
        if x == k:
            answer = []
            while x != n:
                answer.append(x)
                x = visited[x]
            answer.append(i)
            return answer
        if 0<=x-1<=100000 and visited[x-1] == -1:
            q.append(x-1)
            visited[x-1] = x
        if 0<=x*2<=100000 and visited[x*2] == -1:
            # print(x)
            q.append(x*2)
            visited[x*2] = x
        if 0<= x+1 <=100000 and visited[x+1] == -1:
            # print(x)
            q.append(x+1)
            visited[x+1] = x


# def move(i):
#     visited = [-1] * 100001
#     q = deque()
#     q.append((i, [i]))
#     visited[i] = 0
#     while q:
#         x, path = q.popleft()
#         # print(x, q)
#         if x == n:
#             # print(1)
#             return len(path), path
#         if x % 2 == 0:
#             pass
#         else:
#             pass

answer =  move(n, 0)
# move(n)
print(len(answer) - 1)
print(*answer[::-1])


