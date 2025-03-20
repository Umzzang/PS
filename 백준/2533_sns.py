import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())


visited = [0] * (n+1)
tree = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]  # adap , adap x
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(i):
    # print("i",i)
    visited[i] = 1
    cnt = 0
    dp[i][1] = 1
    for j in tree[i]:
        if visited[j] == 1:
            continue
        cnt += 1
        dfs(j)
        dp[i][0] += dp[j][1]
        dp[i][1] += min(dp[j][0], dp[j][1]) 

    if cnt == 0:
        dp[i][0] = 0
        dp[i][1] = 1


dfs(1)
# print(dp)
print(min(dp[1][0], dp[1][1]))
cnt = 0

