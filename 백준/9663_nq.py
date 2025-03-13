n = int(input())
row = [0] *n
def bfs(x):
    global cnt
    if x == n:
        cnt += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if possible(x):
                bfs(x+1)

def possible(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[i]- row[x]) == abs(i-x):
            return False
    return True


cnt = 0


bfs(0)

print(cnt)