import sys
input = sys.stdin.readline

class heap:
    def __init__(self):
        self.heap = [None]
        
    def __str__(self):
        a = ''
        for i in range(1, len(self.heap)):
            a += self.heap[i] + ' '
        return a

    def insert(self, data):
        idx = len(self.heap)
        # print(1, idx)
        self.heap.append(data)
        # print(2, len(self.heap))

        if idx <= 1:
            return
        
        p_idx = idx // 2
        while p_idx>=1 and abs(data) <= abs(self.heap[p_idx]):
            if abs(data) < abs(self.heap[p_idx]):
                self.heap[idx], self.heap[p_idx] = self.heap[p_idx], self.heap[idx]
                idx = p_idx
                p_idx = idx//2
            else:
                if data < self.heap[p_idx]:
                    self.heap[idx], self.heap[p_idx] = self.heap[p_idx], self.heap[idx]
                    idx = p_idx
                    p_idx = idx//2
                else:
                    return

        # print(3, len(self.heap))
        return
    

    def com(self, idx):
        l_idx, r_idx = idx * 2, idx * 2 + 1

        if len(self.heap) <= l_idx:
            return False
        elif len(self.heap) <= r_idx:
            if abs(self.heap[idx]) > abs(self.heap[l_idx]):
                return 1
            elif abs(self.heap[idx]) == abs(self.heap[l_idx]):
                if self.heap[idx] > self.heap[l_idx]:
                    return 1
                else:
                    return False
            else:
                return False
        
        else:
            # 오른쪽 절대값이 왼쪽 절대값보다 클 때
            if abs(self.heap[l_idx]) < abs(self.heap[r_idx]):
                if abs(self.heap[idx]) > abs(self.heap[l_idx]):
                    return 1
                elif abs(self.heap[idx]) == abs(self.heap[l_idx]):
                    if self.heap[idx] > self.heap[l_idx]:
                        return 1
                    else:
                        return False
                else:
                    return False
            # 오른쪽 왼쪽 절대값 같을 때
            elif abs(self.heap[l_idx]) == abs(self.heap[r_idx]):
                if self.heap[l_idx] < self.heap[r_idx]:
                    if abs(self.heap[idx]) > abs(self.heap[l_idx]):
                        return 1
                    elif abs(self.heap[idx]) == abs(self.heap[l_idx]):
                        if self.heap[idx] > self.heap[l_idx]:
                            return 1
                        else:
                            return False
                    else:
                        return False
                elif self.heap[r_idx] < self.heap[l_idx]:
                    if abs(self.heap[idx]) > abs(self.heap[r_idx]):
                        return 2
                    elif abs(self.heap[idx]) == abs(self.heap[r_idx]):
                        if self.heap[idx] > self.heap[r_idx]:
                            return 2
                        else:
                            return False
                    else:
                        return False
                else:
                    if abs(self.heap[idx]) > abs(self.heap[l_idx]):
                        return 1
                    elif abs(self.heap[idx]) == abs(self.heap[l_idx]):
                        if self.heap[idx] > self.heap[l_idx]:
                            return 1
                        else:
                            return False
                    else:
                        return False
            # 왼쪽 절대값이 더 클때
            else:
                if abs(self.heap[idx]) > abs(self.heap[r_idx]):
                    return 2
                elif abs(self.heap[idx]) == abs(self.heap[r_idx]):
                    if self.heap[idx] > self.heap[r_idx]:
                        return 2
                    else:
                        return False
                else:
                    return False
            


    def pop(self):
        if len(self.heap) == 1:
            return 0
        elif len(self.heap) == 2:
            min = self.heap[1]
            del self.heap[1]
            return min
        else:
            min = self.heap[1]
            self.heap[1] = self.heap[-1]
            del self.heap[-1]

            idx = 1
            l_idx, r_idx = idx * 2, idx * 2 + 1
            x = self.com(idx)
            
            while x:
                if x == 1:
                    self.heap[idx], self.heap[l_idx] = self.heap[l_idx], self.heap[idx]
                    idx = l_idx
                else:
                    self.heap[idx], self.heap[r_idx] = self.heap[r_idx], self.heap[idx]
                    idx = r_idx
                x = self.com(idx)
                l_idx, r_idx = idx * 2, idx*2 + 1

            return min






n = int(input())



h = heap()
for _ in range(n):
    x = int(input())
    if x == 0:
        print(h.pop())
    else:
        h.insert(x)
    


