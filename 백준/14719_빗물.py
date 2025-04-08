import sys

input = sys.stdin.readline

def rain(i,j):
    cnt = 1
    rj, lj = j, j
    rj += 1
    while rj<m:
        if area[i][rj] == 1:
            break
        else:
            area[i][rj] = 2
            cnt += 1
        rj += 1
    else:
        cnt = 0
    lj -= 1
    while lj >=0:
        if area[i][lj] == 1:
            break
        else:
            area[i][lj] = 2
            cnt += 1
        lj -= 1
    else:
        cnt = 0
    return cnt


def main():
    global n, m, area
    n, m = map(int,input().split())
    block = list(map(int, input().split()))
    answer = 0
    area = [[0] * m for _ in range(n)]
    for i in range(len(block)):
        for j in range(block[i]):
            area[j][i] = 1
    
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                answer += rain(i,j)
    print(answer)
        

            

if __name__ == "__main__":
    main()