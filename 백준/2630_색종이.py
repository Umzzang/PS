import sys

input = sys.stdin.readline
n = int(input())

paper = []
blue = 0
white = 0
def check(i, j ,n):
    start = paper[i][j]
    for x in range(i,i+n):
        for y in range(j, j+n):
            if paper[x][y] != start:
                return False, start
    return True, start

for _ in range(n):
    paper.append(list(map(int, input().split())))



def cut(n, start, end , blue, white):
    # print(n, start,end)
    if n == 1:
        # print(start,end,n)
        if paper[start][end] == 1:
            return 1,0
        else:
            return 0,1
    result, color = check(start, end, n)
    if result:
        # print("?", start, end, n)
        if color == 1:
            return 1,0
        else:
            return 0,1
    else:
        tb = blue
        tw = white
        a, b = cut(n//2,start,end ,blue,white)
        tb += a
        tw += b
        # print(blue, white)
        a, b = cut(n//2,start+n//2,end,blue,white)
        tb += a
        tw += b
        # print(blue, white)
        a, b = cut(n//2,start,end+n//2,blue,white)
        tb += a
        tw += b
        # print(blue, white)
        a, b = cut(n//2,start+n//2,end+n//2,blue,white)
        tb += a
        tw += b
        # print(blue, white)

    return tb, tw
        


blue,white = cut(n, 0,0, 0,0)
print(white)
print(blue)