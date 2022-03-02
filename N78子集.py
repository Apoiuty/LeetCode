from typing import List


def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    for i in nums:
        for item in res[:]:
            res.append(item + [i])

    return res


print(subsets(0, [1, 2, 3]))
