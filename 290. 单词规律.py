class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(pattern) != len(s):
            return False

        mp1 = {}
        mp2 = {}
        for p, word in zip(pattern, s):
            if p in mp1 and mp1[p] != word or word in mp2 and mp2[word] != p:
                return False
            else:
                mp1[p] = word
                mp2[word] = p

        return True
