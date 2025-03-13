from typing import Optional, TypeVar, Generic

T=TypeVar('T')

class Node:
    __slots__ = ['item', 'pointer']

    def __init__(self, item, pointer:Optional["Node"]=None):
        self.item = item
        self.pointer:Optional["Node"] = pointer

class LinkedList:
    def __init__(self):
        self.head:Optional[Node] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0 
        cur_node:Node = self.head
        length:int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            length += 1
        return length
    
    def __str__(self) -> str:
        if self.head is None:
            return "Empty"
        cur_node:Node = self.head
        result:str = ""
        while cur_node.pointer is not None:
            result += f"{cur_node.item} -> "
            cur_node = cur_node.pointer
        result += str(cur_node.item)
        return result


class Stack(LinkedList):

    def push(self, item)->None:
        new_node: Node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def pop(self):
        if self.head is None:
            raise ValueError("Stack is empty")
        else:
            cur_node:Node = self.head
            if cur_node.pointer is None:
                self.head = None
                return cur_node.item
            while cur_node.pointer.pointer is not None:
                cur_node = cur_node.pointer
            item = cur_node.pointer.item
            cur_node.pointer = None
            return item


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    stack.pop()
    print(stack)
    print(stack.length)

