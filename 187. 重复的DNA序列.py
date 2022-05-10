from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        seen = set()
        for i in range(0, len(s) - 9):
            sub_str = s[i:i + 10]
            if hash(sub_str) in seen:
                result.add(sub_str)
            else:
                seen.add(hash(sub_str))

        return list(result)

s=Solution()
print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))