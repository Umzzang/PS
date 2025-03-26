import sys
import heapq
input = sys.stdin.readline

n = int(input())

small = []
big = []

for _ in range(n):
    a = int(input())
    # if len(small) == 0:
    #     heapq.heappush(small, -a)
    #     print(a)
    #     continue
    # elif 


    if len(small) <= len(big): # small 넣을 차례
        if len(big) == 0:
            heapq.heappush(small, -a)
        else:
            if a > big[0]:
                b = heapq.heappop(big)
                heapq.heappush(big, a)
                heapq.heappush(small, -b)
            else:
                heapq.heappush(small, -a)
    else:       # big넣을 차례
        if a < -small[0]:
            b = heapq.heappop(small)
            heapq.heappush(small, -a)
            heapq.heappush(big, -b)
        else:
            heapq.heappush(big, a)

    
    print(-small[0])