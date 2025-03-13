n = int(input())

treedic = {}

for _ in range(n):
    p, c1, c2 = input().split()
    treedic[p] = [0, 0]
    if c1 != '.':
        treedic[p][0] = c1
    else:
        treedic[p][0] = False
        
    if c2 != '.':
        treedic[p][1] = c2
    else:
        treedic[p][1] = False
        
# print(treedic)
ans1 = ''
ans2 = ''
ans3 = ''
def first(i):
    if not i :
        return
    global ans1
    
    ans1 += i
    first(treedic[i][0])
    first(treedic[i][1])

def second(i):
    global ans2
    if not i:
        return
    second(treedic[i][0])
    ans2 += i
    second(treedic[i][1])

def third(i):
    global ans3
    if not i:
        return
    third(treedic[i][0])
    third(treedic[i][1])
    ans3 += i

first('A')
second('A')
third('A')
print(ans1)
print(ans2)
print(ans3)