def prime_factorize(n: int) -> list[int]:
    """
    素因数分解

    Parameters
    ----------
    N: int
        分解する整数

    Returns
    -------
    list[int]
        素因数のリスト
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
