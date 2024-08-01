import sys
from collections import deque
import time

input = sys.stdin.readline


def mul(x: int) -> int:
    return x * 2


def plus(x: int) -> int:
    return int(str(x) + "1")


def main():
    a, b = map(int, input().split())
    q = deque()
    q.append((a, 1))
    while q:
        # print(q)
        tmp, cnt = q.popleft()
        if tmp == b:
            print(cnt)
            break
        elif tmp < b:
            q.append((mul(tmp), cnt + 1))
            q.append((plus(tmp), cnt + 1))

    else:
        print(-1)


def main2():
    a, b = map(int, input().split())
    cnt = 1
    result = -1
    while a != b:
        if b < a:
            result = -1
            break
        elif b % 10 == 1:
            b = b // 10
            cnt += 1
        elif b % 2 == 0:
            b = b // 2
            cnt += 1
        else:
            result = -1
            break
        result = cnt

    print(result)


if __name__ == "__main__":
    main2()
