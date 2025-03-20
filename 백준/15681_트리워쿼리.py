import sys
sys.setrecursionlimit(10**5 + 10)
input = sys.stdin.readline

n, r, q= map(int, input().split())
tree = [[] for _ in range(n+1)]
dp = [0] * (n+1)
visited = [0] * (n+1)
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    visited[start] = 1
    dp[start] = 1
    for child in tree[start]:
        if visited[child] == 1:
            continue
        dfs(child)
        dp[start] += dp[child]

dfs(r)


for _ in range(q):
    node = int(input())
    print(dp[node])