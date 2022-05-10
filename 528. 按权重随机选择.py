from typing import List
from random import randint
import bisect
from random import randrange
from itertools import accumulate
from random import choices


class Solution:

    def __init__(self, w: List[int]):
        self.weight = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect.bisect_right(self.weight, randrange(0, self.weight[-1]))


s = Solution([1, 2, 3])
result = []
for i in range(6000):
    result.append(s.pickIndex())
from collections import Counter

cnt = Counter(result)
print(cnt)
