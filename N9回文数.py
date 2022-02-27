def isPalindrome(self, x: int) -> bool:
    x = str(x)
    n = len(x)
    if not n % 2:
        return x[:n // 2] == x[:n // 2 - 1:-1]
    else:
        return x[:n // 2] == x[:n // 2:-1]


print(isPalindrome(0, 1221))
