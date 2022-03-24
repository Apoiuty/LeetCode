class Solution:
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = Solution.SYMBOL_VALUES
        ans = 0
        for i, digit in enumerate(s):
            if i < len(s) - 1:
                if SYMBOL_VALUES[s[i]] < SYMBOL_VALUES[s[i + 1]]:
                    ans += -SYMBOL_VALUES[s[i]]
                else:
                    ans += SYMBOL_VALUES[s[i]]
            else:
                ans += SYMBOL_VALUES[s[i]]

        return ans


s = Solution()
print(s.romanToInt("MCMXCIV"))
