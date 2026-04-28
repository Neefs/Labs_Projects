# A class that stores key-value pairs
class Entry:
    def __init__(self, the_key, the_value):
        self.key = the_key
        self.value = the_value

    def __str__(self):
        return str(self.key) + " : " + str(self.value)


# Implements the Mapping ADT:
# Stores the key-value pairs in a list
class ListMapping:
    def __init__(self):
        # Initialize an empty list to store the data
        self._entries = []

    # Add a new or update a key-value pair
    def put(self, key, value):
        e = self._entry(key)
        # If the key is present in the list
        if e is not None:
            # Update the value
            e.value = value
        else:
            # If the key was not present in the list: Add it
            self._entries.append(Entry(key, value))
            
    # Access the value associated with a given key
    def get(self, key):
        e = self._entry(key)
        # If the key is found in the list
        if e is not None:
            # Return the associated value
            return e.value
        else:
            # Else: Raise a KeyError
            raise KeyError

    # Private helper method:
    # Returns the entry associated with a given key, or None if the key is not in the mapping
    def _entry(self, key):
        # Loop through all entries
        for e in self._entries:
            # Until we find the key
            if e.key == key:
                return e
        # If the key was not found
        return None

    # Implements the to-string conversion of the mapping
    def __str__(self):
        return str([str(e) for e in self._entries])

    # Implements the evaluation of self[key]
    def __getitem__(self, key):
        return self.get(key)

    # Implements the assignment self[key] = value
    def __setitem__(self, key, value):
        self.put(key, value)

    # Implements the built-in function len()
    def __len__(self):
        return len(self._entries)

    # Implements the membership test operator: keyword in (and not in)
    def __contains__(self, key):
        if self._entry(key) is None:
            return False
        else:
            return True

    # Returns an iterator: iterates over the keys in the mapping
    def __iter__(self):
        return (e.key for e in self._entries)

    # Returns an iterator: iterates over the values in the mapping
    def values(self):
        return (e.value for e in self._entries)

    # Returns an iterator: iterates over the key-value pairs in the mapping
    def items(self):
        return ((e.key, e.value) for e in self._entries)




class HashMapping:
    def __init__(self, size = 2):
        self._size = size
        self._buckets = [ListMapping()]*self._size
        self._length = 0
 
    def _bucket(self, key):
        return self._buckets[hash(key)%self._size]
 
    def rehash(self):
        # TODO: Implement this method
        self._size *= 2
        new_buckets = [ListMapping() for _ in range(self._size)]
        for lm in self._buckets:
            for k, v in lm.items():
                new_buckets[hash(k)%self._size].put(k, v)
        self._buckets = new_buckets




if __name__ == "__main__":
    hm = HashMapping(size=2)
    hm._buckets[0].put("apple", 1)
    hm._buckets[1].put("banana", 2)
    hm._length = 2

    print("Before rehash:")
    print("Size:", hm._size)
    for i, bucket in enumerate(hm._buckets):
        print(f"Bucket {i}:", bucket)

    hm.rehash()

    print("\nAfter rehash:")
    print("Size:", hm._size)
    for i, bucket in enumerate(hm._buckets):
        print(f"Bucket {i}:", bucket)