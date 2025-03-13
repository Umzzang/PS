import sys
input = sys.stdin.readline
n,c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

# 집 사이 거리
start = 1
end = house[-1] - house[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = house[0]

    for i in range(1, n):
        if house[i] >= current + mid:
            cnt += 1
            current = house[i]
    
    if cnt >= c:
        start = mid + 1
        result = mid
    elif cnt < c:
        end = mid-1
print(result)


