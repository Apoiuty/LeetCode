from collections import defaultdict


class MyHashMap:

    def __init__(self):
        self.divisor = 786433
        self.hashmap = [0] * self.divisor

    def put(self, key: int, value: int) -> None:
        set_value = False
        if self.hashmap[key % self.divisor]:
            for i, [k, v] in enumerate(self.hashmap[key % self.divisor]):
                if k == key:
                    self.hashmap[key % self.divisor][i] = [key, value]
                    set_value = True
                    break
            if not set_value:
                self.hashmap[key % self.divisor].append([key, value])
        else:
            self.hashmap[key % self.divisor] = [[key, value]]

    def get(self, key: int) -> int:
        i = key % self.divisor
        if self.hashmap[i] == 0:
            return -1
        else:
            for i, [k, v] in enumerate(self.hashmap[i]):
                if k == key:
                    return v

        return -1

    def remove(self, key: int) -> None:
        i = key % self.divisor
        if self.hashmap[key]:
            index_to_remove = None
            for i, [k, v] in enumerate(self.hashmap[i]):
                if k == key:
                    index_to_remove = i

            if index_to_remove is not None:
                self.hashmap[key][index_to_remove:index_to_remove + 1] = []


s = MyHashMap()
s.put(1, 1)
s.put(2, 2)
print(s.get(1))
print(s.get(3))
s.put(2, 1)
s.remove(2)
print(s.get(2))
