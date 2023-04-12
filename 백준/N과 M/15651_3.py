n, m = map(int, input().split())

arr = [i for i in range(n+1)]

cnt = 0

answer = []
def c(i):
    
    if i > m:
        print(*answer)
        return
    for j in range(1, n+1):
        answer.append(j)
        c(i+1)
        answer.pop()


c(1)
