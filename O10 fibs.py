def fib(self, n: int) -> int:
    fib = [0, 1]
    if n <= 1:
        return fib[n]
    fn = 0
    fnn = 1
    for i in range(n - 1):
        fnn, fn = fnn + fn, fnn
    return int(fnn % 1e9+7)


print(fib(0, 2))
