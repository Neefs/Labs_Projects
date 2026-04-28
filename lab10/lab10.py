# This file contains the Priority Queue implementations

class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item


class PQ_UL:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))

    def find_min(self):
        if not self._entries:
            raise ValueError("Priority queue is empty")
        return min(self._entries)

    def remove_min(self):
        if not self._entries:
            raise ValueError("Priority queue is empty")
        min_entry = self.find_min()
        self._entries.remove(min_entry)
        return min_entry


class PQ_OL:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._entries.sort()

    def find_min(self):
        if not self._entries:
            raise ValueError("Priority queue is empty")
        return self._entries[0]

    def remove_min(self):
        if not self._entries:
            raise ValueError("Priority queue is empty")
        return self._entries.pop(0)
    