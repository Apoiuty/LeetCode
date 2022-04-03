class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList):
        self.cnt = True
        self.iterator = self._next(nestedList)

    def next(self) -> int:
        return self.next_value

    def _next(self, item):
        if item.isInteger():
            yield item.getInteger()
        else:
            item = item.getList()
            for i in item:
                yield from self._next(i)

    def hasNext(self) -> bool:
        try:
            self.next_value = next(self.iterator)
            return True
        except StopIteration:
            return False


s = NestedIterator([[1, 1], 2, [1, 1]])
while s.hasNext():
    print(s.next())
