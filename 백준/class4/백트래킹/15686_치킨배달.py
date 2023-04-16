import sys

input = sys.stdin.readline

n, m = map(int, input().split())

house = []
chicken = []

def distance(i, j, x, y):
    return abs(i-x) + abs(j-y)

minV = 100000000
def d(i, start):
    global minV
    if i == m:
        # print(checked)
        dis = [100000000000] * len(house)
        for j in range(len(chicken)):
            if checked[j] == 1:
                
                for k in range(len(house)):
                    di = distance(house[k][0], house[k][1], chicken[j][0], chicken[j][1])
                    if dis[k] > di:
                        dis[k] = di
        s = sum(dis)
        if minV > s:
            minV = s
        return
    
    

    for j in range(start, len(chicken)):
        if checked[j] == 0:
            checked[j] = 1
            d(i+1, j+1)
            checked[j] = 0


for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            house.append((i+1, j+1))
        elif arr[j] == 2:
            chicken.append((i+1, j+1))

checked = [0] * len(chicken)

d(0, 0)

print(minV)