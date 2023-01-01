def prime_factorize(N):
    """
    素因数分解

    Parameters
    ----------
    N : int
        分解する整数
    """
    ans = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue

        e = 0
        while N % p == 0:
            e += 1
            N //= p

        ans.append((p, e))
    if N != 1:
        ans.append((N, 1))
    return ans
