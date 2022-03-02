import time


def wordBreak(self, s: str, wordDict) -> bool:
    print(s)
    time.sleep(0.1)
    if not s:
        return True
    wordDict = set(wordDict)
    i = 0
    j = 1
    n = len(s)
    while j <= n:
        if s[i:j] in wordDict:
            has_end = wordBreak(0, s[j:], wordDict)
            if has_end:
                return True
        j += 1

    return False


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
print(wordBreak(0, s, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
