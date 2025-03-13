import sys
import heapq

input = sys.stdin.readline

t = int(input())
for tc in range(t):
    k = int(input())
    maxheap = []
    minheap = []
    mark = [0] * k
    for i in range(k):
        
        o, n = input().split()
        if o == "I":
            heapq.heappush(minheap, (int(n), i))
            heapq.heappush(maxheap, (-int(n), int(n), i))
            mark[i] = 1
        else:
            if n == "-1":
                
                while minheap and mark[minheap[0][1]] == 0:
                    heapq.heappop(minheap)
                if minheap:
                    mark[minheap[0][1]] = 0
                    heapq.heappop(minheap)

            else:
                while maxheap and mark[maxheap[0][2]] == 0:
                    heapq.heappop(maxheap)
                if maxheap:
                    mark[maxheap[0][2]] = 0
                    heapq.heappop(maxheap)
    while minheap and mark[minheap[0][1]] == 0: heapq.heappop(minheap)
    
    while maxheap and mark[maxheap[0][2]] == 0: heapq.heappop(maxheap)
    
    if len(maxheap) == 0 or len(minheap) == 0:
        print('EMPTY')
    else:
        print(maxheap[0][1], minheap[0][0])