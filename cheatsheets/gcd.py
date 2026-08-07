def GCD(A, B):
    """
    最大公約数
    """
    if B == 0:
        return A
    else:
        return GCD(B, A % B)
