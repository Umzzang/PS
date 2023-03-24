import heapq
import sys
input = sys.stdin.readline

# 직접 구현

# class Heap:
    # def __init__(self):
    #     self.heap = []
    #     self.heap.append(None)
    
    # def insert(self, data):
    #     self.heap.append(data)
    #     idx = len(self.heap) - 1
    #     if idx == 1:
    #         return
        
    #     p_idx = idx//2
    #     while p_idx>0 and self.heap[p_idx] < self.heap[idx]:
    #         self.heap[idx], self.heap[p_idx] = self.heap[p_idx], self.heap[idx]
    #         idx = p_idx
    #         p_idx = idx//2
    #     return
    
    # def com(self, idx):
    #     l_idx, r_idx = idx * 2, idx * 2 + 1
    #     if l_idx >= len(self.heap):
    #         return False
    #     elif r_idx >= len(self.heap):
    #         if self.heap[l_idx] > self.heap[idx]:
    #             return 1
    #         else:
    #             return False
    #     else:
    #         if self.heap[l_idx] > self.heap[r_idx]:
    #             if self.heap[l_idx] > self.heap[idx]:
    #                 return 1
    #             else:
    #                 return False
    #         else:
    #             if self.heap[r_idx] > self.heap[idx]:
    #                 return 2
    #             else:
    #                 return False

    # def pop(self):
    #     if len(self.heap) == 1:
    #         return 0
        
    #     max = self.heap[1]
    #     self.heap[1] = self.heap[-1]
    #     del self.heap[-1]

    #     idx = 1

    #     l_idx, r_idx = idx * 2, idx * 2 + 1

    #     x = self.com(idx)

    #     while x:
    #         if x == 1:
    #             self.heap[l_idx], self.heap[idx] = self.heap[idx], self.heap[l_idx]
    #             idx = l_idx
    #         else:
    #             self.heap[r_idx], self.heap[idx] = self.heap[idx], self.heap[r_idx]
    #             idx = r_idx

    #         l_idx, r_idx = idx * 2, idx * 2 + 1

    #         x = self.com(idx)

    #     return max


# heapq 모듈 사용 heapq는 최소힙 => 최대힙 하려면 튜플로

heap = []

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

for num in arr:

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
        
    else:
        heapq.heappush(heap, (-num, num))