from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushed.reverse()
        popped.reverse()
        while popped:
            if stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
                continue
            else:
                if not pushed:
                    return False
            if pushed:
                stack.append(pushed.pop())

        return True


s = Solution()
print(s.validateStackSequences([2, 1, 0], [1, 2, 0]))
