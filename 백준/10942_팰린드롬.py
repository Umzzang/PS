import sys
input = sys.stdin.readline
n = int(input())
lst = [0] + list(map(int, input().split()))
m = int(input())

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dp[i][j] = 1
        if j == i+1:
            if lst[j] == lst[i]:
                dp[i][j] = 1
for i in range(2, n):
    for j in range(1, n-i+1):
        if lst[j] == lst[j+i] and dp[j+1][j+i-1]:
            # print(i,j)
            dp[j][j+i] = 1
# print(dp)


# def check(i, j):
#     i += 1
#     j -= 1
#     while i <= j:
#         if lst[i] == lst[j]:
#             i += 1
#             j -= 1
#             continue
#         else:
#             return False
#     return True
        


# def change(i,j):
#     while i<=j:
#         dp[i][j] = 1
#         i += 1
#         j -= 1

# for i in range(1, n+1):
#     for j in range(n, i-1, -1):
#         if lst[i] == lst[j]:
#             # print(i,j)
#             if check(i,j):
#                 # print(i,j)
#                 change(i,j)

# # print(dp)
for _ in range(m):
    a,b = map(int,input().split())
    print(dp[a][b])