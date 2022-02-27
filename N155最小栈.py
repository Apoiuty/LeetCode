import math


class MinStack:

    def __init__(self):
        self.min_index = 0
        self.min_value = math.inf
        self.stack = []

    def push(self, val: int) -> None:
        if val < self.min_value:
            self.min_value = val
            self.min_index = len(self.stack)
        self.stack.append((val, self.min_index))

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.min_index = self.stack[-1][1]
            self.min_value = self.stack[self.min_index][0]
        else:
            self.min_index = 0
            self.min_value = math.inf

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[self.stack[-1][1]][0]


a = MinStack()
a.push(-10)
a.push(-10)
print(a.getMin(), a.getMin())
a.push(-20)
print(a.getMin(), a.getMin(), a.top(), a.getMin(), a.pop())
a.push()
