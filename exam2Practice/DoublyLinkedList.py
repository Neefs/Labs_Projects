 
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev # left direction
        self.next = next
 
 
class DLL:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, item:Node):
        self.size += 1
        if self.is_empty():
            self._head, self._tail = item
            return
        self._head.prev = item
        item.next = self._head
        self._head = item
        self._head.prev = None #Incase prev was previsioly set to something else

    def remove_first(self):
        if self.is_empty():
            return None
        item = self._head
        if self.size == 1:
            self._head, self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self.size -=1
        return item
    
    def add_last(self, item):
        if self.is_empty():
            self._head, self._tail = item
            self.size+=1
            return
        self._tail.next = item
        item.prev = self._tail
        self._tail = item
        item.next = None
        self.size += 1
        

def binary_search_rec(L:list, item:int):
    """Assuming L is a sorted int array"""
    if len(L) == 0:
        return False
    median = len(L) // 2
    if item == L[median]:
        return True
    if item > L[median]:
        return binary_search_rec(L[median+1:], item)
    elif item < L[median]:
        return binary_search_rec(L[:median], item)


print(binary_search_rec([i for i in range(10**6)], 1097400))