a = input()
b = input()
m = len(a)
n = len(b)
arr = [[0] * (m +1) for _ in range(n+1)]
maxv = 0
for i in range(n):
    for j in range(m):
        if a[j] == b[i]:
            arr[i+1][j+1] = arr[i][j] + 1
            if arr[i+1][j+1] > maxv:
                maxv = arr[i+1][j+1]
        else:
            arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])

ans = ''

i = n
j = m
while i>=0 and j>=0:
    start = arr[i][j]
    if arr[i-1][j] == arr[i][j]:
        i -= 1
    elif arr[i][j-1] == arr[i][j]:
        j -= 1
    else:
        ans = a[j-1] + ans
        i -= 1
        j -= 1
print(ans)

print(maxv)