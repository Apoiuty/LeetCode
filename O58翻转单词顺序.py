class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

s=Solution()
print(s.reverseWords("the sky is blue"))
