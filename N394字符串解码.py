class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            letter = s[i]
            if letter.isalpha():
                stack.append(letter)
            elif letter.isdigit():
                item = ''
                while s[i].isdigit() and i < n:
                    item += s[i]
                    i += 1
                stack.append(item)
                continue
            elif letter == ']':
                string = ''
                item = stack.pop()
                while not item.isdigit():
                    string = item + string
                    item = stack.pop()
                string = int(item) * string
                stack.append(string)
            i += 1

        return ''.join(stack)


s = Solution()
print(s.decodeString("100[leetcode]"))
