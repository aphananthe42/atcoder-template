from math import factorial


def comb(n, r):
    """
    nCrを求める
    """
    return factorial(n) // factorial(n - r) // factorial(r)
