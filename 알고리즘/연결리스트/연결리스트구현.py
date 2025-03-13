class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.idx = 0


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        cur = self.head
        s = ''
        if cur is None:
            ss = f'[{s}]'
            return ss
        else:
            while cur.next is not None:
                s += str(cur.data) + ', '
                cur = cur.next
            s += str(cur.data) 
            ss = f'[{s}]'

        return ss

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            cur = self.head
            idx = 0
            while cur.next is not None:
                idx += 1
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            cur.next.idx = idx
            
            self.tail = new_node    
        self.len += 1
        

    def insert(self, idx, data):
        if self.len < idx:
            print('error')
            return
        elif self.len == idx:
            new_node = Node(data)
            self.tail.next = new_node
            self.len += 1


        else:
            cur = self.head
            cnt = 1
            for _ in range(idx+1):
                if cnt == idx:
                    new_node = Node(data) 
                    new_node.next = cur.next
                    cur.next = new_node
                    break
                cur = cur.next
                cnt += 1
            self.len += 1


            

l = LinkedList()
l.append(8)
l.append(9)
l.append(123)
l.insert(5,1)
print(len(l))
print(l)
l.insert(3,1111)
print(len(l))
print(l)
l.insert(2, 22222)
print(l)