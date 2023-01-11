import sys
n = int(sys.stdin.readline())

a, b = n // 5, n % 5

if b == 0:
    print(a)
elif b == 1:
    a -= 1
    if a >= 0:
        print(a + 2)
    else:
        print(-1)
elif b == 2:
    a -= 2
    if a >= 0:
        print(a + 4)
    else:
        print(-1)
elif b == 3:
    print(a + 1)
elif b == 4:
    a -= 1
    if a >= 0:
        print(a + 3)
    else:
        print(-1)