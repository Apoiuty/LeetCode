from typing import List


def generateParenthesis(self, n: int) -> List[str]:
    result = []
    current_result = ''
    stack = [['', 0]]
    while stack:
        tmp = stack.pop()
        level = tmp[1]
        tmp = tmp[0]
        # 先验证再展开
        current_result = current_result[:level - 1]
        left_cnt = current_result.count('(')
        right_cnt = current_result.count(')')
        if tmp == '(':
            if not left_cnt < n:
                continue
        elif tmp == ')':
            if not left_cnt > right_cnt:
                continue
        current_result += tmp

        # 失败或是到达栈底回溯
        if len(current_result) == n * 2:
            result.append(current_result)
            right_cnt -= 1
        # 深度优先遍历
        if level < 2 * n:
            stack.extend([[')', level + 1], ['(', level + 1]])

    return result


print(generateParenthesis(0, 4))
