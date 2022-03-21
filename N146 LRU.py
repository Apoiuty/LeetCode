class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key)


class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.lru = OrderedDict()
        self.cnt = 0

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            self.lru.move_to_end(key)
        else:
            self.lru[key] = value
            if self.cnt < self.capacity:
                self.cnt += 1
            else:
                del self.lru[list(self.lru.keys())[0]]


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
