import unittest
from linkedlist import *


class TestNode(unittest.TestCase):
    def test_init(self):
        """Tests the initialization of a Node."""
        node1 = Node("Hello")
        node2 = Node("Two", node1)
        self.assertEqual(node1.item, "Hello")
        self.assertEqual(node1.link, None)
        self.assertEqual(node2.item, "Two")
        self.assertEqual(node2.link, node1)

    def test_repr(self):
        """Tests the string representation of a Node."""
        node1 = Node("Hello")
        self.assertEqual(repr(node1), "Node(Hello)")

class TestLinkedList(unittest.TestCase):
    def test_init_empty(self):
        """Tests the initialization of an empty LinkedList."""
        LL1 = LinkedList()
        self.assertEqual(len(LL1), 0)
        self.assertEqual(LL1.get_head(), None)
        self.assertEqual(LL1.get_tail(), None)

    def test_init_filled(self):
        """Tests the initialization of a filled LinkedList."""
        LL1 = LinkedList([1, 2, 3])
        self.assertEqual(len(LL1), 3)
        self.assertEqual(LL1.get_head(), 1)
        self.assertEqual(LL1.get_tail(), 3)

    def test_add_last(self):
        """Tests adding items to the end of the LinkedList."""
        LL1 = LinkedList()
        for i in range(10):
            LL1.add_last(i)
            self.assertEqual(len(LL1), i+1)
            self.assertEqual(LL1.get_head(), 0),
            self.assertEqual(LL1.get_tail(), i)
        self.assertEqual(LL1.get_head(), 0)

    def test_add_first(self):
        """Tests adding items to the front of the LinkedList."""
        LL1 = LinkedList()
        for i in range(10):
            LL1.add_first(i)
            self.assertEqual(len(LL1), i+1)
            self.assertEqual(LL1.get_head(), i)
            self.assertEqual(LL1.get_tail(), 0)
        self.assertEqual(LL1.get_tail(), 0)

    def test_remove_first(self):
        """Tests removing items from the front of the LinkedList."""
        L = [1, 2, 3, 4, 5]
        LL1 = LinkedList(L)
        for i in L:
            self.assertEqual(LL1.get_head(), i)
            self.assertEqual(LL1.remove_first(), i)
            self.assertEqual(len(LL1), len(L) - L.index(i) - 1)
            self.assertEqual(LL1.get_head(), L[L.index(i) + 1] if L.index(i) + 1 < len(L) else None)
            self.assertEqual(LL1.get_tail(), 5 if len(LL1) > 0 else None)
        self.assertEqual(len(LL1), 0)

    def test_remove_last(self):
        """Tests removing items from the end of the LinkedList."""
        L = [1, 2, 3, 4, 5]
        LL1 = LinkedList(L)
        for expected in reversed(L):
            self.assertEqual(LL1.get_tail(), expected)
            self.assertEqual(LL1.remove_last(), expected)
            self.assertEqual(len(LL1), L.index(expected))
            self.assertEqual(LL1.get_tail(), L[L.index(expected) - 1] if L.index(expected) - 1 >= 0 else None)
            self.assertEqual(LL1.get_head(), 1 if len(LL1) > 0 else None)
        self.assertEqual(len(LL1), 0)


unittest.main()