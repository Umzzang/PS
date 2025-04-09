import sys
input = sys.stdin.readline

def check(arr, k):
    cnt = 0
    for n in arr:
        if n == 0:
            cnt += 1
    if cnt >= k:
        return False
    return True

def rotate(i,n):
    i -= 1
    if i < 0:
        i = 2*n-1
    return i

def robotmove(i, n):
    i += 1
    if i > 2*n -1:
        i = 0
    return i 

def main():
    n, k = map(int, (input().split()))
    belt = list(map(int, (input().split())))
    robots = []
    up = 0
    down = n-1
    d = []
    cnt = 0
    while check(belt, k):
        cnt += 1
        up, down = rotate(up,n), rotate(down,n)
        for i in range(len(robots)-1, -1, -1):
            robot = robots[i]
            nextrobot = robotmove(robot, n)
            if robot == down:
                robots.pop()
                continue
            if belt[nextrobot] != 0 and nextrobot not in robots:
                belt[nextrobot] -= 1
                if nextrobot == down:
                    robots.pop()
                else:
                    robots[i] = nextrobot
        if belt[up] != 0:
            robots = [up] + robots
            belt[up] -= 1
        # if len(d) != 0:
        #     for i in range(len(d), -1, -1):
        #         robots.pop(i)
        #     d = []
        # print(belt, robots, up, down)
    print(cnt)

if __name__ == "__main__":
    main()