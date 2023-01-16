def eratosthenes(N):
    """
    エラトステネスの篩
    1以上N以下の数が素数かどうかを返す

    Parameters
    ----------
    N: int
        判定する上限
    """
    table = [True] * (N + 1)
    table[0], table[1] = False, False

    for p in range(2, N + 1):
        if not table[p]:
            continue
        q = p * 2
        while q <= N:
            table[q] = False
            q += p
    return table
