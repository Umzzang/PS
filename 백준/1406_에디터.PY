import sys

input = sys.stdin.readline

s = input().rstrip()

cursorleft = list(s)
cursorright = []
# print(cursorleft)
n = int(input())
for _ in range(n):
    command = input().rstrip()
    if command[0] == 'L':
        if cursorleft:
            cursorright.append(cursorleft.pop())
        else:
            continue
    elif command[0] == 'D':
        if cursorright:
            cursorleft.append(cursorright.pop())
        else:
            continue
    elif command[0] == 'B':
        if cursorleft:
            cursorleft.pop()
    else:
        _, word = command.split(' ')
        cursorleft.append(word)

answer = "".join(cursorleft) + "".join(reversed(cursorright))
print(answer)
