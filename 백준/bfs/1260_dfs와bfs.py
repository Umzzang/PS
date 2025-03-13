from collections import deque
import sys

def main():
    global visited, answer, graph
    # n, m, v = map(int, input().split(' '))
    n, m, v = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        fir, sec = map(int, input().split(' '))
        graph[fir].append(sec)
        graph[sec].append(fir)

    for ele in graph:
        ele.sort()
    visited = [0] * (n+1)
    answer = ''
    dfs2(v)
    # print(len(answer))
    # print(len(answer.rstrip()))
    print(answer)
    visited = [0] * (n+1)
    answer = ''
    bfs(v)
    print(answer)


def bfs(start):
    global answer
    q = deque()
    q.append(start)
    visited[start] = 1
    
    while q:
        nc = q.popleft()
        answer += f'{nc} '
        for num in graph[nc]:
            if visited[num] == 0:
                q.append(num)
                visited[num] = 1


def dfs2(start):
    global answer
    stack = [start]
    
    while stack:
        nc = stack.pop()
        
        if visited[nc] == 0:
            answer += f'{nc} '
            visited[nc] = 1
            stack += reversed(graph[nc])
        


def dfs(start):
    global answer
    if visited[start] == 1:
        return
    
    answer += f'{start} '
    visited[start] = 1
    for num in graph[start]:
        if visited[num] == 0:
            dfs(num)
    


if __name__ == "__main__":
    main()