import sys

input = sys.stdin.readline

n = int(input())


def find(x):
    if friend[x] != x:
        friend[x] = find(friend[x])
    return friend[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        friend[y] = x
        number[x] += number[y]
    print(number[x])


for _ in range(n):
    m = int(input())
    friend, number = {}, {}
    for _ in range(m):
        a, b = input().split()
        if friend.get(a) is None:
            friend[a] = a
            number[a] = 1
        if friend.get(b) is None:
            friend[b] = b
            number[b] = 1
        

        union(a,b)