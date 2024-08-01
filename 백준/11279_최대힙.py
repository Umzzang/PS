import heapq
import sys

input = sys.stdin.readline
def main():
    n = int(input())
    method = 1
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    if method:
        h = MaxHeap()
        for x in arr:
            if x == 0: 
                if h.length() > 1:
                    value = h.pop()
                    print(value)
                else:
                    print(0)
            else:
                h.insert(x)

    else:
        h = []
        for x in arr:
            if x == 0:
                if len(h) > 0:
                    value = heapq.heappop(h)
                    print(-value)
                else:
                    print(0)
            else:
                heapq.heappush(h, -x)


class MaxHeap:
    def __init__(self) -> None:
        self.heap = [None]

    def length(self):
        return len(self.heap)

    def insert(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1
        parent_idx = idx // 2
        while parent_idx >= 1  and self.heap[parent_idx] < self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
            idx = parent_idx
            parent_idx = idx // 2

    def com(self, idx):
        lidx = idx * 2
        ridx = lidx + 1

        if len(self.heap) - 1 >= ridx:
            if self.heap[lidx] > self.heap[ridx]:
                if self.heap[lidx] > self.heap[idx]:
                    return 1
                else:
                    False
            else:
                if self.heap[ridx] > self.heap[idx]:
                    return 2
                else:
                    False
        
        elif len(self.heap) - 1 == lidx:
            if self.heap[lidx] > self.heap[idx]:
                return 1
            else:
                return False
        else: return False


    def pop(self):
        maxValue = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]

        idx = 1
        x = self.com(idx)

        while x:
            if x == 1:
                self.heap[idx], self.heap[idx*2] = self.heap[idx*2], self.heap[idx]
                idx *= 2
            elif x == 2:
                self.heap[idx], self.heap[idx*2+1] = self.heap[idx*2+1], self.heap[idx]
                idx = idx * 2 + 1
            x = self.com(idx)

        return maxValue

if __name__ == "__main__":
    main()