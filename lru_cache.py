class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}              # key -> Node

        # dummy nodes so I never have to handle None pointers
        self.head = Node()           # least recently used side
        self.tail = Node()           # most recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # unlink the node from wherever it is in the list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_end(self, node):
        # put the node just before tail (most recently used spot)
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)       # it was just used
        return node.value

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_end(node)
            return

        if len(self.cache) >= self.capacity:
            lru = self.head.next     # first real node = least recently used
            self._remove(lru)
            del self.cache[lru.key]

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_end(node)
    
c = LRUCache(2)
c.put(1, 10)
c.put(2, 20)
assert c.get(1) == 10        # key 1 is now most recently used
c.put(3, 30)                 # evicts key 2
assert c.get(2) == -1
c.put(1, 99)                 # update existing key
assert c.get(1) == 99
assert c.get(3) == 30

print("All LRU Cache tests passed!")