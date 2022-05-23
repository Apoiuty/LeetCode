class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        str_hash = 0
        n = len(s)
        p_k = 1
        for i in range(n - k, n):
            str_hash += ((ord(s[i]) - 96) % modulo) * (p_k % modulo) % modulo
            p_k = (p_k * (power % modulo)) % modulo

        result = None
        str_hash %= modulo
        if str_hash == hashValue:
            result = s[n - k:n]

        p_m = power % modulo

        for i in reversed(range(0, n - k)):
            str_hash *= p_m
            str_hash -= (ord(s[i + k]) - 96) * p_k
            str_hash += ord(s[i]) - 96
            str_hash %= modulo
            if str_hash == hashValue:
                result = s[i:i + k]

        return result


s = "leetcode"
power = 7
modulo = 20
k = 2
hashValue = 0
s_ = Solution()
print(s_.subStrHash(s, power, modulo, k, hashValue))
