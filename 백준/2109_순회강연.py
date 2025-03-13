import sys
import heapq

input = sys.stdin.readline
n = int(input())
pd = []
for _ in range(n):
    pd.append(list(map(int, input().split())))

pd.sort(key=lambda x: x[1],reverse=True)
temp = []
for pay, day in pd:
    heapq.heappush(temp, -pay)

    



# temp = []
# pd.sort(key=lambda x : x[1])

# for pay, day in pd:
#     heapq.heappush(temp, pay)

#     while len(temp) > day:
#         heapq.heappop(temp)

# print(sum(temp))
