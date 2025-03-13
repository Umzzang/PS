import sys
input = sys.stdin.readline

n, k = map(int, input().split())

bag = []

for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))


arr = [[0] * (k+1) for _ in range(n+1)]
# 첫 풀이 => 1 ~ k 까지 무게에 대하여 계속 bag 순환 => 똑같은 물건 두번 담길수도 있음
# for i in range(1, k+1):
    
#     for j in range(n):
#         w, v = bag[j]
#         if w > i:
#             continue
#         else:
#             arr[i] = max(arr[i], v + arr[i-w])


for i in range(1, n+1):
    w, v = bag[i-1]
    for j in range(1, k+1):
        if w > j:
            arr[i][j] = arr[i-1][j]
        else:
            # 한줄 그전거랑 비교해야함
            arr[i][j] = max(arr[i-1][j], v + arr[i-1][j-w])


print(arr[n][k])
# print(arr)
