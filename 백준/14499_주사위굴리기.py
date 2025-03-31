import sys
input = sys.stdin.readline

dice = [[0] * 3 for _ in range(3)]
dicetop = 0
def move(q, ni, nj, dicetop):
    value = area[ni][nj]
    if value == 0:
        if q ==1:
            newdice = [dice[1][1], dice[1][2], dicetop]
            dicetop = dice[1][0]
            dice[1] = newdice
        elif q == 2:
            newdice = [dicetop, dice[1][0], dice[1][1]]
            dicetop = dice[1][2]
            dice[1] = newdice
        elif q ==3:
            dice[0][1], dice[1][1], dice[2][1], dicetop = dicetop, dice[0][1], dice[1][1],  dice[2][1]
        elif q ==4:
            dice[0][1], dice[1][1], dice[2][1], dicetop = dice[1][1], dice[2][1], dicetop, dice[0][1]
        area[ni][nj] = dice[1][1]
    else:
        if q == 1:
            newdice = [dice[1][1], value, dicetop]
            dicetop = dice[1][0]
            dice[1] = newdice
        elif q == 2:
            newdice = [dicetop, value, dice[1][1]]
            dicetop = dice[1][2]
            dice[1] = newdice
        elif q == 3:
            dice[0][1], dicetop = dicetop, dice[2][1]
            dice[2][1] = dice[1][1]
            dice[1][1] = value
        elif q == 4:
            dice[2][1], dicetop = dicetop, dice[0][1]
            dice[0][1] = dice[1][1]
            dice[1][1] = value
        area[ni][nj] = 0

        
    return dicetop
n, m, x, y,k = map(int, input().split())
dir = [0, [0,1],[0,-1], [-1,0], [1,0]]
area = []



for _ in range(n):
    area.append(list(map(int, input().split())))

quiz = list(map(int, input().split()))
i, j = x, y
for q in quiz:
    di, dj = dir[q]
    ni, nj = i+ di, j + dj
    if 0<=ni<n and 0<=nj<m:
        dicetop = move(q, ni, nj, dicetop)
        # print(q,dice, dicetop)
        print(dicetop)
        i,j = ni,nj

