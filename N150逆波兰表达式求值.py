from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item.isdigit() or item[1:].isdigit():
                stack.append(int(item))
            else:
                if item == '+':
                    stack.append(stack.pop() + stack.pop())
                if item == '-':
                    stack.append(-stack.pop() + stack.pop())
                if item == '*':
                    stack.append(stack.pop() * stack.pop())
                if item == '/':
                    stack.append(int(1 / stack.pop() * stack.pop()))

        return stack[0]


s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
