n, x = map(int, input().split())

level = [0] * 51
level[0] = 1
bread = [0] * 51
bread[0] = 0
patty = [0] * 51
patty[0] = 1
for i in range(1, 51):
    level[i] = level[i-1] * 2 + 3
    bread[i] = bread[i-1] * 2 + 2
    patty[i] = level[i] - bread[i]
# print(level)
# print(bread)
# print(patty)
# print(level[3])
answer = 0
def devide(l, cnt):
    # print(l, cnt)
    if cnt == 0:
        return 0
    if l == 0:
        return 1
    hamburger = level[l]
    cnt -= 1
    prev = (hamburger-3)//2
    if cnt > prev:
        return devide(l-1, cnt-prev-1) + patty[l-1] + 1
    elif cnt < prev:
        return devide(l-1, cnt)
    else: 
        return patty[l-1]
    

    


answer += devide(n, x)
print(answer)