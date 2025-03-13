from typing import Generic, TypeVar, Optional

T = TypeVar("T", int, str, list)


class Node(Generic[T]):

    def __init__(self, data: T, pointer: Optional["Node"] = None) -> None:
        self.data = data
        self.pointer = pointer


class LinkedList(Generic[T]):

    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        current_node = self.head
        cnt = 1
        while current_node.pointer:
            current_node = current_node.pointer
            cnt += 1
        return cnt
