class MaxHeap:
    def __init__(self) -> None:
        self.heap = [None]


    def check_swap_up(self, idx):
        if idx  == 1:
            return False
        parent_idx = idx // 2
        if self.heap[parent_idx] < self.heap[idx]:
            return True
        else:
            return False 
        
        

    def insert(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1
        while self.check_swap_up(idx):
            parent_idx = idx // 2
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx //= 2


    def com(self, idx):
        l_idx = idx * 2
        r_idx = l_idx + 1

        if len(self.heap) - 1 >= r_idx:
            # 둘다 있을 때
            if self.heap[l_idx] > self.heap[r_idx]:
                if self.heap[idx] > self.heap[l_idx]:
                    return 1
                else:
                    return False
            elif self.heap[l_idx] < self.heap[r_idx]:
                if self.heap[idx] > self.heap[r_idx]:
                    return 2
                else:
                    return False

        elif len(self.heap) - 1 >= l_idx:
            if self.heap[l_idx] > self.heap[idx]:
                return 1
            else:
                return False

        else:
            return False


    def delete(self):
        if len(self.heap) == 1:
            return
        
        maxValue = self.heap[1]
        self.heap[1] = self.heap[-1]
        del self.heap[-1]

        idx = 1
        x = self.com(idx)
        while x:
            if x == 1:
                self.heap[idx], self.heap[idx*2] = self.heap[idx*2], self.heap[idx]
                idx = idx*2
            elif x == 2:
                self.heap[idx], self.heap[idx*2+1] = self.heap[idx*2+1], self.heap[idx]
                idx = idx*2 + 1
            x = self.com(idx)
        return maxValue
