class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        version1 = [int(i) for i in version1]
        version2 = [int(i) for i in version2]
        from itertools import zip_longest
        for num1, num2 in zip_longest(version1, version2, fillvalue=0):
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1

        return 0


s = Solution()
version1 = "0.1"
version2 = "1.1"
print(s.compareVersion(version1, version2))
