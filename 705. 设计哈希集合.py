from collections import defaultdict


class MyHashSet:

    def __init__(self):
        self.hashSet = defaultdict(list)
        self.divisor = 786433

    def add(self, key: int) -> None:
        hash_num = key % self.divisor
        if not self.contains(key):
            self.hashSet[hash_num].append(key)

    def remove(self, key: int) -> None:
        hash_num = key % self.divisor
        try:
            self.hashSet[hash_num].remove(key)
        except ValueError:
            pass

    def contains(self, key: int) -> bool:
        hash_num = key % self.divisor
        return key in self.hashSet[hash_num]
