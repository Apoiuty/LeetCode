from typing import List


def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)
    digits[-1] += 1
    for i in range(n):
        item = digits[n - i - 1]
        if item < 10:
            return digits
        else:
            if n - i - 2 >= 0:
                digits[n - i - 2] += 1
                digits[n - i - 1] -= 10

    if digits[0] >= 10:
        digits[0] -= 10
        digits[0:0] = [1]

    return digits


print(plusOne(0, [9, 9, 9]))
