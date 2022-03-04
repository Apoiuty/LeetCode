def myPow(x: float, n: int) -> float:
    # x==0
    if not x or not n:
        return 1
    if n == 1:
        return x

    sign = -1 if n < 0 else 1
    n = abs(n)
    result = myPow(x, n // 2)
    result *= result
    if n  & 1:
        result *= x

    return result if sign == 1 else 1 / result


print(myPow(2, 10))

