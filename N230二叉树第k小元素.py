class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        num_stack = []
        op_stack = []
        neg_num = False
        s = s.strip()
        while i < len(s):
            if s[i].isdigit():
                digit = ''
                while i < len(s) and s[i].isdigit():
                    digit += s[i]
                    i += 1
                if not neg_num:
                    num_stack.append(int(digit))
                else:
                    num_stack.append(-int(digit))
                    neg_num = False
                # 乘除法直接计算
                if op_stack and op_stack[-1] in '*/':
                    op = op_stack.pop()
                    op1 = num_stack.pop()
                    op2 = num_stack.pop()
                    if op == '*':
                        num_stack.append(op1 * op2)
                    else:
                        num_stack.append(int(op2 / op1))
            elif s[i] == ' ':
                i += 1
                continue
            elif s[i] in '+-*/':
                if s[i] == '-':
                    neg_num = True
                    if i != 0:
                        op_stack.append('+')
                    i += 1
                    continue
                op_stack.append(s[i])
                i += 1
        while op_stack:
            op = op_stack.pop()
            op1 = num_stack.pop()
            # 开头加法
            op2 = num_stack.pop()
            if op == '+':
                num_stack.append(op1 + op2)
            else:
                num_stack.append(op2 - op1)

        return num_stack[0]


s = Solution()
print(s.calculate("14-3/2"))
