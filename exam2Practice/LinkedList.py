

class Node:
    def __init__(self, value):
        self.next: Node = None
        self.value = value

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self, n:Node):
        if self._head != None:
            n.next = self._head
            self._head = n
            self._len += 1
        else:
            self._head = n

    