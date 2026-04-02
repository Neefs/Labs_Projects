
class Queue:
    def __init__(self):
        self._L = []
        self._head = 0
        self._len = 0

    @classmethod
    def from_list(cls, l:list):
        ret = cls()
        ret._L = l
        ret._len = len(l)
        return ret


    def __len__(self):
        return self._len
    
    def is_empty(self):
        return self._len == 0

    def enqueue(self, item):
        self._L.append(item)
        self._len += 1
    
    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        self._len -= 1
        if self._head > (len(self._L)//2):
            self._L = self._L[self._head:]
            self._head = 0
        return item
    
l = [i for i in range(10)]
print(l)
q = Queue.from_list(l)

for i in l:
    print(q.dequeue())
print(q.is_empty())



"""

Queue using Python list with lazy delete (efficient dequeue)
Implement a Queue class using a Python list and a “lazy delete” strategy. Your implementation must support:
enqueue(x) in O(1) amortized time
dequeue() in O(1) amortized time using a front index (raise an exception if empty)
is_empty() and __len__() in O(1)

Requirements:
Do not use pop(0) or del a[0].
Use an integer head index to track the logical front.
Include a cleanup step: when head becomes large relative to the list size (e.g., head > len(L)//2), compact the list and reset front.

"""