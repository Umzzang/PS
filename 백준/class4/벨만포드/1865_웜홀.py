import sys

input = sys.stdin.readline

tc = int(input())
inf = 100000000000000
def search(start):
    dis = [inf] * (n+1)
    dis[start] = 0
    
    for i in range(n):
        for edge in graph:
            cur = edge[0]
            end = edge[1]
            time = edge[2]
            if  dis[cur] != inf and dis[end] > dis[cur] + time:
                dis[end] = dis[cur] + time
                
    return dis[start]



for _ in range(1, tc + 1):
    ans = "NO"
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, t*-1))

    
    # 이렇게 모든노드 검색은 시간초과
    # 모든 노드에 대해 조사할 필요 x, 음수사이클 존재만 파악하면 무조건 회귀가능
    for i in range(1, n+1):
        result = search(i)
        if result < 0:
            ans = 'YES'
            break
    print(ans)

    # 아래가 정답
    # if search(1) < 0:
    #     print('YES')
    # else:
    #     print('NO')        
    