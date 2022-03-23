from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i, t))
            else:
                _, last_t = stack[-1]
                if last_t >= t:
                    stack.append((i, t))
                else:
                    while last_t < t:
                        stack.pop()
                        answers[_] = i - _
                        if stack:
                            _, last_t = stack[-1]
                        else:
                            break

                    stack.append((i, t))


        return answers


s = Solution()
print(s.dailyTemperatures([30, 60, 90]))
