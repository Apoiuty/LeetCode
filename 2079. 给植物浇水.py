from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cnt = 0
        i = 0
        n = len(plants)
        cur_c = capacity
        while i < n:
            if plants[i] <= cur_c:
                cnt += 1
                cur_c -= plants[i]
            else:
                cnt += i + 1 + i
                cur_c = capacity - plants[i]
            i += 1

        return cnt


s = Solution()
print(s.wateringPlants([1, 1, 1, 4, 2, 3], 4))
