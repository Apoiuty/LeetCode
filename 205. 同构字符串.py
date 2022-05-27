from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        for i, j in zip(s, t):
            if i in mp1 and mp1[i] != j or j in mp2 and mp2[j] != i:
                return False
            else:
                mp1[i] = j
                mp2[j] = i

        return True


s = Solution()
print(s.isIsomorphic('badc', 'baba'))
