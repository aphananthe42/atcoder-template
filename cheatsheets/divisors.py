def enumerate_divisors(N):
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


def count_devisors(N):
    """
    約数の個数

    Parameters
    ----------
    N: int
        判定する整数
    """
    count = 0
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        count += 1
        if N // i != i:
            count += 1
    return count
