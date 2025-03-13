# import sys
# input = sys.stdin.readline

# n = int(input())

# s= []

# for _ in range(n):
#     s.append(list(map(int, input().split())))

# answer = sys.maxsize
# visited = [0] * n
# def dfs(cnt, index):
#     global answer
   
#     if cnt == n//2:
#         a = 0
#         b = 0
#         for j in range(n):
#             for jj in range(n):
#                 if visited[j] and visited[jj]:
#                     a += s[j][jj]
#                 elif not visited[j] and not visited[jj]:
#                     b += s[j][jj]
#         # print(index, a, b)
#         answer = min(answer, abs(a-b))
#         return
    
#     for i in range(index, n):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(cnt+1, i)
#             visited[i] = 0


# dfs(0,0)
# print(answer)



import sys
from itertools import combinations
N = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(list(zip(stat, zip(*stat))))
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 대각선끼리 합
print(sum_stat)
allstat = sum(sum_stat) // 2 # 모든 값 합의 절반
print(allstat)
s=0
for i in range(N):
    for j in range(N):
        s+=stat[i][j]
print(s)
result = float('inf')
for l in combinations(sum_stat, N//2): # 대각선 합에서 뽑은 2개 중에서
    result = min(result, abs(allstat - sum(l))) # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀
print(result)