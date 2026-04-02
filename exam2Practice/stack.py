

"""
Stack using Python list (efficient push/pop)
Implement a Stack class using a Python list. Your implementation must support:
push(x) in O(1)
pop() in O(1) (raise an exception if empty)
is_empty() in O(1) time
__len__() in O(1) tim
"""
class Stack:
    def __init__(self):
        self._L:list = []
        

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        return self._L.pop()
    
    def __len__(self):
        return len(self._L)

    def is_empty(self):
        return len(self) == 0
    

ns = Stack()
ns.push(len)
ns.push(print)
ns.push(print)

ns.pop()("hello")
ns.pop()(ns.pop()("hello"))

print(ns.pop())