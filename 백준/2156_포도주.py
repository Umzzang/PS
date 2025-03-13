import sys

input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def drink(sum, c, i):
#     if i >= n:
#         return sum
#     if c == 2:
#         return drink(sum, 0, i+1)
#     return max(drink(sum + wine[i], c+1, i+1), drink(sum, 0, i+1))

n = int(input())
# 0 ~ n-1
wine = []
answer = [0] * (n+1)
for _ in range(n):
    wine.append(int(input()))

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:

    answer[1] = wine[0]
    answer[2] = wine[0] + wine[1]   
    answer[3] = max(wine[0] + wine[2], wine[1] + wine[2], answer[2])

    for i in range(4, n+1):
        answer[i] = max(answer[i-1], answer[i-2] + wine[i-1], answer[i-3] + wine[i-2]+ wine[i-1])

    print(answer[n])

