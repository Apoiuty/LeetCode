from typing import *
# 2022-04-13 18:13:57	

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        try:
            nums.index(target)
            return True
        except:
            return False
# leetcode submit region end(Prohibit modification and deletion)

        pass