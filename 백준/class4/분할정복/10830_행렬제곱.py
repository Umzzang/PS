import sys
input = sys.stdin.readline

n, b = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
base = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            base[i][j] = 1
# print(list(zip(*arr)))
def mul(arr):
    re_arr = list(zip(*arr))
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        row = arr[i]
        for j in range(n):
            col = re_arr[j]
            cnt = 0
            for k in range(len(row)):
                cnt += row[k] * col[k]
            new_arr[i][j] = cnt % 1000
    return new_arr

def m(arr1, arr2):
    re_arr = list(zip(*arr2))
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        row = arr1[i]
        for j in range(n):
            col = re_arr[j]
            cnt = 0
            for k in range(len(row)):
                cnt += row[k] * col[k]
            new_arr[i][j] = cnt % 1000
    return new_arr



def r(arr, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr
    
    tmp = r(arr, b//2)
    if b%2==0:
        return mul(tmp)
    else:
        return m(mul(tmp), arr)
    









# 첫 풀이 (시간초과)
# i= 1
# cnt = 0
# while i < b:
#     i *= 2
#     cnt += 1



# dp = [0] * cnt


# s = 0
# for i in range(cnt-1, -1, -1):
#     if 2 ** i <= b:
#         dp[i] = 1
#         b -= 2 ** i
#     if b == 0:
#         break
# last = 0

# for i in range(cnt):
#     if dp[i] == 1:
#         for _ in range(i-last):
#             arr = mul(arr) 
            
#         last = i
        
#         base = m(base, arr)
        
base = r(arr, b)
for i in range(n):
    print(*base[i])
