from typing import *
from itertools import combinations


# 2022-04-13 17:46:42

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for item in combinations(range(1, 1 + n), k):
            ans.append(list(item))

        return ans

        # leetcode submit region end(Prohibit modification and deletion)
