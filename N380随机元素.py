class RandomizedSet:

    def __init__(self):
        self.index_hash = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.index_hash:
            return False
        else:
            self.index_hash[val] = len(self.data)
            self.data.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.index_hash:
            self.index_hash[self.data[-1]] = self.index_hash[val]
            self.data[-1], self.data[self.index_hash[val]] = self.data[self.index_hash[val]], self.data[-1]
            self.data.pop()
            del self.index_hash[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        from random import choice
        return choice(self.data)


s = RandomizedSet()
s.insert(0)
s.insert(1)
s.remove(0)
s.insert(2)
s.remove(1)
print(s.getRandom())
