def numTrees(self, n: int) -> int:
    d = [1, 1]
    for i in range(2, n + 1):
        cnt = 0
        for j in range(i):
            cnt += d[j] * d[i - j - 1]
        d.append(cnt)

    return d[-1]


print(numTrees(0, 1))
