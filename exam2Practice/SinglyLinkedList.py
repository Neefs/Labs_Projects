

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value) + " In __str__"

 

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, item):
        if self._head is None:
            self._head = item
            self._tail = item
            self.size += 1  
            return
        item.next = self._head
        self.size += 1  
        self._head = item

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        item = self._head
        self._head = self._head.next
        self.size -= 1
        if self.size <= 1:
            self._tail = self._head
        return item
    
    def add_last(self, item):
        if self.is_empty():
            self._head = item
            self._tail = item
            self.size += 1
            return
        self._tail.next = item
        self._tail = item
        self.size += 1

    def remove_last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        item = self._tail
        if self._head == item:
            self._head = None
            self._tail = None
            return item
        temp = self._head
        while (temp.next != None and temp.next != item):
            temp = temp.next
        self._tail = temp
        self.size -= 1
        return item
        

ll = LinkedList()
rl = [i+1 for i in range(5)]
for i in rl:
    ll.add_last(Node((i)))
print(ll._tail, ll._head)
l2 = []
for i in rl:
    t = ll.remove_last()
    l2.append(t.value)
    print(t)
    print(ll.size, ll._head, ll._tail)
print(rl, l2)


        
        
             

