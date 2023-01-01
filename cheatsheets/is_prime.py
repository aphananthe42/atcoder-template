def is_prime(N):
    """
    素数判定

    Parameters
    ----------
    N : int
        判定する整数
    """
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True
