class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num2.startswith('0') or num1.startswith('0'):
            return '0'

        num1 = list(int(i) for i in num1)
        num2 = list(int(i) for i in num2)

        result = []
        for i in reversed(range(len(num2))):
            cnt = len(num2) - i
            for num in reversed(num1):
                add_sum = num * num2[i]
                if len(result) < cnt:
                    result.append(add_sum)
                else:
                    result[cnt - 1] += add_sum
                # cnt是从右到左的位数
                cnt += 1
        for i in range(len(result)):
            if result[i] >= 10:
                if i < len(result) - 1:
                    result[i + 1] += result[i] // 10
                else:
                    result.append(result[i] // 10)
                result[i] %= 10

        result = [str(i) for i in result]
        result = ''.join(reversed(result))
        return result


s = Solution()
print(s.multiply('123', '456'))
