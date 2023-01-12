from collections import deque
import sys
n = int(sys.stdin.readline())

q = deque()

for i in range(n):
    n = int(sys.stdin.readline())
    if n == 0:
        q.pop()
    else:
        q.append(n)
print(sum(q))