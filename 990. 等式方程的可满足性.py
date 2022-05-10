from typing import List
from collections import defaultdict


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eq_union_set = defaultdict(set)
        for eq in equations:
            sign = eq[1:3]
            a, b = eq[0], eq[-1]

            if sign == '!=':
                if a == b:
                    return False
                if eq_union_set[a] and eq_union_set[b]:
                    # 违反了相等性判断
                    if eq_union_set[a] == eq_union_set[b]:
                        return False

                if not eq_union_set[a]:
                    eq_union_set[a].add(a)
                if not eq_union_set[b]:
                    eq_union_set[b].add(b)
            else:
                if a == b:
                    continue
                if eq_union_set[a] and eq_union_set[b]:
                    # 违反了相等性判断
                    if eq_union_set[a] != eq_union_set[b]:
                        return False
                if not eq_union_set[a]:
                    eq_union_set[b].add(a)
                    eq_union_set[a] = eq_union_set[b]
                if not eq_union_set[b]:
                    eq_union_set[a].add(b)
                    eq_union_set[b] = eq_union_set[a]
        return True


s = Solution()
print(s.equationsPossible(["c==c", "f!=a", "f==b", "b==c"]))
