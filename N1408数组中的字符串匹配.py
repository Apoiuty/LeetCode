from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        all_word = ',' + ','.join(sorted(words, key=lambda x: -len(x))) + ','
        ans = []
        for word in words:
            i = all_word.find(word)
            if all_word[i - 1] != ',' or all_word[i + len(word)] != ',':
                ans.append(word)

        return ans


s = Solution()
print(s.stringMatching(["mass", "as", "hero", "superhero"]))
