import sys

input = sys.stdin.readline

n,k = map(int, input().split())

coins = []
answer = [k+1] * (k+1) # answer[i] 는 i 만드는 최소값
answer[0] = 0
for _ in range(n):
    coins.append(int(input()))


for coin in coins:
    # print(answer)
    for i in range(coin, k+1):
        answer[i] = min(answer[i], answer[i-coin]+1)

# print(answer)
if answer[k] == k+1:
    print(-1)
else:
    print(answer[k])












# coins.sort()

# def det(cost, coinindex):

#     cnt = cost // coins[coinindex]
#     restcost = cost - coins[coinindex] * cnt
    
#     if answer[restcost] == k+1:
#         return k+1
    
#     else:
#         return min(answer[cost], cnt + answer[restcost])
    

# for j in range(len(coins)):
#     for i in range(coins[j], k+1):
#         if i % coins[j] == 0:
#             answer[i] = min(answer[i], i//coins[j])
#         else:
#             if j == 0:
#                 continue
#             else:
#                 answer[i] = min(answer[i], det(i, j))


# if answer[k] == k+1:
#     print(-1)
# else:
    
#     print(answer[k])

