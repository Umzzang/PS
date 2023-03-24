t = int(input())
for test in range(1, t+1):
    n = int(input())
    board = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        r1, c1, r2, c2, c = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if board[i][j] != c and board[i][j] != 0:
                    board[i][j] = 3
                else:
                    board[i][j] = c
    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                cnt += 1

    print(f'#{test} {cnt}')
    
    