def calc_divisors(N):
    """
    約数列挙

    Parameters
    ----------
    N: int
        判定する整数
    """
    ans = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        ans.append(i)
        if N // i != i:
            ans.append(N // i)
    ans.sort()
    return ans
