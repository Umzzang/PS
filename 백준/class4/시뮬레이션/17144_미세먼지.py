import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
arr = [list(map(int, input().split())) for _ in range(r)]

air_c = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            air_c.append((i, j))





def mise():
    new_arr = [[0] * c for _ in range(r)]
    for i, j in air_c:
        new_arr[i][j] = -1

    def spread(i, j):
        cnt = 0
        res = arr[i][j] // 5   
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0<=ni<r and 0<=nj<c and arr[ni][nj] != -1:
                cnt += 1
                new_arr[ni][nj] += res
        new_arr[i][j] += (arr[i][j] - res * cnt)

    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                spread(i, j)


    return new_arr


def air():
    oj = 0
    new_arr = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            new_arr[i][j] = arr[i][j]

    fir_i = air_c[0][0]
    sec_i = air_c[1][0]
    for j in range(2, c):
        new_arr[fir_i][j] = arr[fir_i][j-1]
        new_arr[sec_i][j] = arr[sec_i][j-1]
    new_arr[fir_i][1], new_arr[sec_i][1] = 0, 0

    for i in range(fir_i-1, -1, -1):
        new_arr[i][c-1] = arr[i+1][c-1]

    for i in range(sec_i+1, r):
        new_arr[i][c-1] = arr[i-1][c-1]

    for j in range(c-2, -1, -1):
        new_arr[0][j] = arr[0][j+1]
        new_arr[r-1][j] = arr[r-1][j+1]
    
    for i in range(1, fir_i):
        new_arr[i][0] = arr[i-1][0]
    for i in range(r-2, sec_i, -1):
        new_arr[i][0] = arr[i+1][0]
    

    for i, j in air_c:
        new_arr[i][j] = -1


    return new_arr




i = 0

while i<t:
    # for i in range(r):
    #     print(*arr[i])
    # print()
    arr = mise()
    # for i in range(r):
    #     print(*arr[i])
    # print()
    arr = air()
    # for i in range(r):
    #     print(*arr[i])
    # print()
    i += 1

s = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != -1:
            s += arr[i][j]

print(s)