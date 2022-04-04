class Solution:
    def countPrimes(self, n: int) -> int:
        a = {i: 0 for i in range(2, n)}
        primer = []
        for i in range(2, n):
            if a[i] == 0:
                primer.append(i)

            for k in primer:
                val = k * i
                if val < n:
                    a[val] = 1
                    if i % k == 0:
                        break
                else:
                    break

        return len(primer)


s = Solution()
ans = []
for i in range(0, 5 * 10 ** 6 + 1):
    print(i)
    ans.append(s.countPrimes(i))

print(ans)
