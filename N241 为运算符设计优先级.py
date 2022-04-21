from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def diff_compute(sub_expression: str):
            if sub_expression.isdigit():
                return [int(sub_expression)]

            result = []
            for i, s in enumerate(sub_expression):
                if sub_expression[i] in '+-*':
                    op=sub_expression[i]
                    left_op = diff_compute(sub_expression[:i])
                    right_op = diff_compute(sub_expression[i + 1:])
                    for l in left_op:
                        for r in right_op:
                            if op=='-':
                                result.append(l-r)
                            if op=='*':
                                result.append(l*r)
                            if op=='+':
                                result.append(l+r)


            return result

        return diff_compute(expression)


s = Solution()
print(s.diffWaysToCompute("0"))
