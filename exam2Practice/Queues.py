

class Queue:
    def __init__(self):
        self.head = 0
        self._L = []

    def enqueue(self, element):
        self._L.append(element)

    def lazydequeue(self): #O(1)
        i = self._L[self.head]
        self.head += 1
        return i
    
  