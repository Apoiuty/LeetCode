class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i for i in reversed(s.strip().split())])
