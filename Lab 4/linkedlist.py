from typing import Any, Iterable, Optional

class Node:
    def __init__(self, item: Any, link=None):
        """Initializes a new node with the given item and link."""
        self.item: Any = item
        if link is not None and type(link) != Node:
            raise TypeError("link must be of type Node or None")
        self.link: Node | None = link

    def __repr__(self):
        """Returns a string representation of the Node."""
        return f"Node({self.item})"
    

class LinkedList:
    def __init__(self, items:Optional[Iterable[Any]]=None) -> None:
        """Initializes a new LinkedList."""
        self._head = None
        self._tail = None

        if items is not None:
            for item in items: 
                self.add_last(item)

    def __len__(self) -> int:
        """Returns the number of items in the LinkedList."""
        count = 0
        node = self._head
        while node is not None:
            count += 1
            node = node.link
        return count
    
    def get_head(self):
        """Gets the first item of the LinkedList"""
        return self._head.item if self._head is not None else None
    
    def get_tail(self):
        """Gets the last item of the LinkedList"""
        return self._tail.item if self._tail is not None else None
    
    def add_last(self, item:Any):
        """Adds an item to the end of the LinkedList"""
        new_node = Node(item)
        if self._is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node

    

    def _is_empty(self):
        return self._head is None

    def add_first(self, item:Any):
        """Adds an item to the front of the LinkedList"""
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head
    
    def remove_first(self):
        """Removes and returns the first item. Raises an error if list is empty."""
        if self._is_empty():
            raise RuntimeError("Cannot remove from an empty list")
        r = self._head
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        return r.item

    def remove_last(self):
        """Removes and returns the last item. Raises an error if list is empty."""
        if self._is_empty():
            raise RuntimeError("Cannot remove from an empty list")
        r = self._tail
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.link is not self._tail:
                current = current.link
            current.link = None
            self._tail = current
        return r.item

LL1 = LinkedList()


s.push('A')
s.push('B')
s.push('C')
s.peek()
s.pop()
s.push('D')
s.pop()
s.pop()
s.peek()
s.pop()
