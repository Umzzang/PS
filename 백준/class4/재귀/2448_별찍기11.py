n = int(input())

arr = [[' '] * (n * 2 - 1) for _ in range(n)]


def star(i, j, n):
    if n == 3:
        arr[i][j] = '*'
        arr[i+1][j-1] = arr[i+1][j+1] = '*'
        for k in range(-2,3):
            arr[i+2][j+k] = '*'
    else:
        n //= 2
        star(i, j, n)
        star(i+n, j - n, n)
        star(i+n, j+n, n)

star(0, n-1, n)
for i in arr:
    print("".join(i))