import string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_index = {s: -1 for s in string.printable}
        result = [0] * (1 + len(s))
        cnt = 0
        for i, letter in enumerate(s):
            before_index = letter_index[letter]
            if before_index == -1:
                result[i] = result[i - 1] + 1
            else:
                distance = i - before_index
                if distance > result[i - 1]:
                    result[i] = result[i - 1] + 1
                else:
                    result[i] = distance
            letter_index[letter] = i
            cnt = max(cnt, result[i])

        return cnt


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
