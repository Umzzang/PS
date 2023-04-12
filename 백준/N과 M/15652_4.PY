n, m = map(int, input().split())

answer = []
def b(i, start):
    if i > m :
        print(*answer)
        return
    
    for j in range(start, n+1):
        answer.append(j)
        b(i+1, j)
        answer.pop()

b(1, 1)
