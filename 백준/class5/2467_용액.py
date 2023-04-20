import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

first = 0
last = n-1

ans = abs(arr[first] + arr[last])
fl = arr[first]
ll = arr[last]
while first < last:
    tmp = arr[first] + arr[last]
    
    if abs(tmp) < ans:
        fl = arr[first]
        ll = arr[last]
        ans = abs(tmp)

    if tmp == 0:
        fl = arr[first]
        ll = arr[last]
        break

    if tmp > 0:
        last -= 1
    else:
        first += 1

print(fl, ll)