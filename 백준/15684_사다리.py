import sys

input = sys.stdin.readline

n,m,h = map(int, input().split())  # n이 세로선 개수 h가 가로선 개수
letter = [[0] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    letter[a][b] = 1  # a 번 가로선  b 번 세로선 b+1 세로선

# x 가 세로 선 번호 linenum 이 가로선 번호
def find(x, linenum):
    if linenum > h:
        return x
    else:
        
        if letter[linenum][x] == 1:
            return find(x+1,linenum+1)
        elif letter[linenum][x-1] == 1:
            return find(x-1, linenum+1)
        else:
            return find(x, linenum+1)

def b():
    for i in range(1, n+1):
        if i == find(i, 1):
            continue
        else:
            return False
    else:
        return True

    
def dfs(cnt, x, y):
    global answer
    
    if answer <= cnt:
        return
    
    if b():
        answer = cnt
        return cnt
    
    if cnt == 3:
        return

    for i in range(x, h+1):
        if i == x:
            now = y
        else:
            now = 1
        for j in range(now, n):
            if letter[i][j] == 0 and letter[i][j+1] == 0:
                if letter[i][j-1]:
                    continue
                letter[i][j] = 1
                dfs(cnt+1, i ,j+2)
                letter[i][j] = 0

answer = 4
dfs(0,1,1)
if answer >3:
    answer = -1
print(answer)

