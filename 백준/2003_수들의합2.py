import sys

input = sys.stdin.readline

n,m = map(int, input().split())

number = list(map(int, input().split()))

cnt = 0

l = 0
r = 0
sum = number[0]
while True:
    try:
        if sum == m:
            cnt +=1
            r+=1
            sum += number[r]
        elif sum < m:
            r += 1
            sum += number[r]
        elif sum > m :
            l += 1
            sum -= number[l-1]
    except:
        break
    


print(cnt)

