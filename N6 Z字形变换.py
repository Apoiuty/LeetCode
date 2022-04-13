class Solution:
    def convert(self, s: str, numRows: int) -> str:

        n = len(s)
        ans = []
        for i in range(numRows):
            if i == 0:
                for j in range(0, n, max(1, 2 * numRows - 2)):
                    ans.append(s[j])
            elif i == numRows - 1:
                for j in range(i, n, 2 * i):
                    ans.append(s[j])
            else:
                first_delta = 2 * (numRows - i - 1)
                second_delta = 2 * i
                j = i
                if j < n:
                    ans.append(s[j])
                while j < n:
                    if j + first_delta < n:
                        j += first_delta
                        ans.append(s[j])
                    else:
                        break
                    if j + second_delta < n:
                        j += second_delta
                        ans.append(s[j])
                    else:
                        break
        return ''.join(ans)


s = Solution()
print(s.convert("AB", 1))
