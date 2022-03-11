from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import bisect
        max_min = arr[0]
        result = []
        for item in arr:
            if len(result) < k:
                bisect.insort_left(result, item)
                if item > max_min:
                    max_min = item
            else:
                if item < max_min:
                    result.pop()
                    bisect.insort_left(result, item)
                    max_min = result[-1]

        return result


s = Solution()
print(s.getLeastNumbers([0, 1, 1, 2, 4, 4, 1, 3, 3, 2], 6))
