class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        from collections import Counter
        cnt = Counter(s)
        less_k = set()
        for key, item in cnt.items():
            if item < k:
                less_k.add(key)

        if not less_k:
            return len(s)
        else:
            max_len = 0
            last_less_k = -1
            for i in range(len(s)):
                if s[i] in less_k:
                    max_len = max(max_len, self.longestSubstring(s[last_less_k + 1:i], k))
                    last_less_k = i
            max_len = max(max_len, self.longestSubstring(s[last_less_k + 1:], k))
            return max_len


s = Solution()
print(s.longestSubstring('ababbc', 2))
