import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []

for _ in range(n):
    ar = list(map(int, input().split()))
    for i in range(1, n):
        ar[i] = ar[i-1] + ar[i]
    if not arr:
        arr.append(ar)
    else:
        a = arr[-1]
        for i in range(n):
            ar[i] = ar[i] + a[i]
        arr.append(ar)

# print(arr)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        print(arr[x2][y2])
    elif x1 == 0 and y1 != 0:
        print(arr[x2][y2] - arr[x2][y1-1])
    elif x1 != 0 and y1 == 0:
        print(arr[x2][y2] - arr[x1-1][y2])
    else:
        print(arr[x2][y2] + arr[x1-1][y1-1] - arr[x2][y1-1] - arr[x1-1][y2] )