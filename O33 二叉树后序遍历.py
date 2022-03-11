from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 2:
            return True

        i = 0
        j = len(postorder) - 2
        root = postorder[-1]
        pre_i = pre_j = None
        while i <= j:
            # 不是二叉树
            if postorder[i] == pre_i and postorder[j] == pre_j:
                return False
            pre_j = postorder[j]
            pre_i = postorder[i]
            if postorder[i] < root:
                i += 1
            if postorder[j] > root:
                j += -1

        return self.verifyPostorder(postorder[:i]) and self.verifyPostorder(postorder[i:-1])


s = Solution()
print(s.verifyPostorder([1,3,2,6,5]))
