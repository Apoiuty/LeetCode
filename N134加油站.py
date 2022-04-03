from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        n = len(gas)
        while i < n:
            # 过不去或是从下一个节点出发也行
            if (gas_gain := gas[i] - cost[i]) < 0:
                i += 1
            else:
                begin = i
                j = (i + 1) % n
                while gas_gain >= 0:
                    gas_gain += gas[j] - cost[j]
                    j = (j + 1) % n
                    if j == begin and gas_gain >= 0:
                        return begin
                if j <= i:
                    return -1
                else:
                    i = j

        return -1


s = Solution()
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
