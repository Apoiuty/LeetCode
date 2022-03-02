from typing import List


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = set()

    def _conbinationSum(choices, n):
        if n == 0 and choices:
            ans.add(tuple(sorted(choices)))
        if n < min(candidates) and min(candidates) >= 0:
            return
        if n > max(candidates) and max(candidates) <= 0:
            return

        for item in candidates:
            _conbinationSum(choices + [item], n - item)

    _conbinationSum([], target)
    return list(list(i) for i in ans)


print(combinationSum(0, [1,2], 3))
