import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == len(self.right_heap):
            if self.right_heap:
                max_min = self.right_heap[0]
                if num > max_min:
                    bisect.insort(self.left_heap, self.right_heap[0])
                    self.right_heap[0:1] = []
                    bisect.insort(self.right_heap, num)
                else:
                    bisect.insort(self.left_heap, num)
            else:
                bisect.insort(self.left_heap, num)
        else:
            min_max = self.left_heap[-1]
            if num < min_max:
                bisect.insort(self.right_heap, self.left_heap[-1])
                self.left_heap[-1:] = []
                bisect.insort(self.left_heap, num)
            else:
                bisect.insort(self.right_heap, num)

    def findMedian(self) -> float:
        if len(self.right_heap) == len(self.left_heap):
            if self.right_heap:
                return (self.right_heap[0] + self.left_heap[-1]) / 2
            else:
                raise 0
        else:
            return self.left_heap[-1]


s = MedianFinder()
s.addNum(-1)
s.addNum(-2)
s.addNum(-3)
s.addNum(-4)
print(s.findMedian())
