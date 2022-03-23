import time


def wordBreak(self, s: str, wordDict) -> bool:
    not_working = set()

    def word_break(s, wordDict):
        if not s:
            return True

        i = 0
        j = 1
        n = len(s)
        while j <= n:
            if s[i:j] in wordDict:
                if s[j:] not in not_working:
                    has_end = word_break(s[j:], wordDict)
                    if has_end:
                        return True
                    else:
                        not_working.add(s[j:])
            j += 1

        not_working.add(s)

    word_break(s, wordDict)
    if s in not_working:
        return False
    else:
        return True


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
print(wordBreak(0, s, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
