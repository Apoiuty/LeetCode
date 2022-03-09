class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        before_sign = False
        after_sign = False
        got_one_dot = False
        got_num_before = False
        for i, item in enumerate(s):
            if not item.isdigit() and item not in '+-eE.':
                return False
            elif item.isdigit():
                got_num_before = True
            elif item == '.':
                # e后面跟小数或是多个点
                if got_one_dot:
                    return False
                got_one_dot = True
            elif item in 'Ee':
                e = s[i + 1:].strip()
                if not s[i + 1:]:
                    return False
                got_one_num = False
                for j, e_item in enumerate(e):
                    if e_item in '+-':
                        if not j and not after_sign:
                            after_sign = True
                        else:
                            return False
                    elif not e_item.isdigit():
                        return False
                    else:
                        got_one_num = True
                if not got_one_num:
                    return False
                else:
                    return True
            elif item in '+-':
                # 开头出现
                if not before_sign and not i:
                    before_sign = True
                else:
                    return False
        return got_num_before


s = Solution()
print(s.isNumber('.'))
