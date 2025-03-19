import sys

input = sys.stdin.readline
dir = ['R', 'D', 'L', 'U']
n = int(input())
area = [[0] * n for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j = map(int, input().split())
    area[i-1][j-1] = 2
l = int(input())
m = {}
for _ in range(l):
    a, b = input().split()
    m[int(a)] = b

time = 0
snake = [[0,0]]

def move(d):
    # print(snake, time)
    if d == 'R':
        newi, newj = snake[-1][0], snake[-1][1] + 1
    elif d== 'D':
        newi, newj = snake[-1][0] +1, snake[-1][1]
    elif d == 'L':
        newi, newj = snake[-1][0], snake[-1][1] - 1
    else:
        newi, newj = snake[-1][0] -1, snake[-1][1]
    
    if 0<=newi<n and 0<=newj<n and (newi, newj) not in snake:
        # print(newi, newj, snake)
        if area[newi][newj] == 2:
            snake.append((newi, newj))
            area[newi][newj] = 0
        else:
            snake.pop(0)
            snake.append((newi,newj))
        return True

    else:
        return False

dindex = 0
while True:
    if m.get(time):
        if m[time] == 'D':
            dindex = (dindex +1)%4
        elif m[time] == 'L':
            dindex = (dindex -1)
            if dindex < 0:
                dindex += 4


    time += 1

    if not move(dir[dindex]):
        break
print(time)