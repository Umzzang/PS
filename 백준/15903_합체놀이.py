import sys
import heapq
input = sys.stdin.readline

n, m  = map(int, input().split())
cards = list(map(int, input().split()))

class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)

    def s(self):
        return sum(self.heap[1:])

    def insert(self, value):
        self.heap.append(value)
        idx = len(self.heap)-1
        if idx <= 1:
            return
        
        p_idx = idx//2
        while p_idx >= 1:
            if self.heap[idx] < self.heap[p_idx]:
                self.heap[idx], self.heap[p_idx] = self.heap[p_idx], self.heap[idx]
                idx = p_idx
                p_idx = idx//2
            else:
                return
        
    def com(self, x):
        l_idx = x *2
        r_idx = l_idx +1
        if len(self.heap) <= l_idx:
            return False
        elif len(self.heap) == l_idx+1:
            if self.heap[x] > self.heap[l_idx]:
                return 1
            else:
                return False
        else:
            if self.heap[l_idx] < self.heap[r_idx]:
                if self.heap[x] > self.heap[l_idx]:
                    return 1
                else:
                    return False
            else:
                if self.heap[x] > self.heap[r_idx]:
                    return 2
                else:
                    return False
    
    def pop(self):
        if len(self.heap) == 1:
            return

        v = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        idx = 1

        l_idx = idx * 2
        r_idx = l_idx +1
        x = self.com(idx)
        while x:
            if x == 1:
                self.heap[l_idx], self.heap[idx] = self.heap[idx], self.heap[l_idx]
                idx = l_idx
            else:
                self.heap[r_idx], self.heap[idx] = self.heap[idx], self.heap[r_idx]
                idx = r_idx
            l_idx = idx * 2
            r_idx = l_idx +1
            x = self.com(idx)
        return v
    
# heap = Heap()

# for card in cards:
#     heap.insert(card)

# for _ in range(m):
#     a = heap.pop()
#     b = heap.pop()
#     heap.insert(a+b)
#     heap.insert(a+b)

# print(heap.s())

heapq.heapify(cards)
for _ in range(m):
    a = heapq.heappop(cards)
    b= heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    heapq.heappush(cards, a+b)
print(sum(cards))