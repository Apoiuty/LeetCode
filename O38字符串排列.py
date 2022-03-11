from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        result = [s]
        for i in range(len(s) - 1):
            for s in result[:]:
                same = set()
                same.add(s[i])
                for j in range(i + 1, len(s)):
                    tmp = list(s)
                    if tmp[j] not in same:
                        same.add(tmp[j])
                        tmp[i], tmp[j] = tmp[j], tmp[i]
                        result.append(''.join(tmp))

        return result


s = Solution()
print(s.permutation('abab'))
