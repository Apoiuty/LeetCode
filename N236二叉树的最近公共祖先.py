class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        head = root
        walked = set()
        p_path = q_path = None
        while head or stack:
            if head:
                stack.append(head)
                if head == p:
                    p_path = stack[:]
                if head == q:
                    q_path = stack[:]

                if p_path and q_path:
                    break
                head = head.left
            else:
                head = stack[-1]
                if head not in walked:
                    walked.add(head)
                    head = head.right
                else:
                    stack.pop()
                    head = None

        cnt = -1
        for i, j in zip(p_path, q_path):
            if i != j:
                break
            cnt += 1

        return p_path[cnt]


from leetcode import *

s = Solution()
root = build_tree([1, 2, null])
print(s.lowestCommonAncestor(root, TreeNode(1), TreeNode(2)))
