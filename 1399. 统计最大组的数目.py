from collections import defaultdict, Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        result = defaultdict(int)
        for i in range(1, n + 1):
            result[sum(int(j) for j in str(i))] += 1

        return Counter(result.values())[max(result.values())]
