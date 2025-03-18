import sys
import heapq

input = sys.stdin.readline

n,m,l = map(int,input().split())

station = list(map(int, input().split()))
station = [0] + station + [l]
station.sort()

temp = []
vmax = 0
for i in range(len(station)-1):
    
    v = station[i+1] - station[i]
    vmax = max(v, vmax)
    heapq.heappush(temp, -v)
# print(station)
# print(temp)

# 큰거 하나씩 빼서 v 보다 작게 만들수 있는지 확인
def find(v, tmp , c):
    a = heapq.heappop(tmp) * -1
    # a는 간격중 가장 긴 구간
    # v는 목표치
    while a > v:
        # print(a, v, c)
        for j in range(c+1):
            if (a) % (j+1) == 0:
                if v >= (a)//(j+1):
                    c -= j
                    if tmp:
                        a = heapq.heappop(tmp) * -1
                    else:
                        return True
                    break

            else:
                if v >= (a)//(j+1) +1:
                    c-=j
                    if tmp:
                        a = heapq.heappop(tmp) * -1
                    else:
                        return True
                    break
        else:
            return False
            
        # if not tmp or c==0:
        #     return False
    
    return True
    






def search(l, r):
    while l <= r:

        mid = (l+r) //2
        # print(l, r, mid)
        result = find(mid, temp[:], m)
        if result:
            r = mid - 1
        else:
            l = mid+1
    return l

answer = search(0, vmax)
print(answer)
