n = int(input())

answer = [[0] * 10 for _ in range(n+1)]
answer[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2, n+1):
    answer[i][0] = answer[i-1][1]
    answer[i][9] = answer[i-1][8]
    for j in range(1,9):
        answer[i][j] = answer[i-1][j-1] + answer[i-1][j+1]


print(sum(answer[n])%1000000000)