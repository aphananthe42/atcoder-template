"""
整数問題リファレンス
"""

import sys


def input():
    return sys.stdin.readline()[:-1]

def is_prime(N):
    """
    素数判定

    Parameters
    ----------
    N : int
        判定する整数
    """

    if N < 2: return False
    i = 2
    while i * i <= N:
        if N % i == 0: return False
        i += 1
    return True

def eratosthenes(N):
    """
    エラトステネスの篩
    1以上N以下の数が素数かどうかを返す

    Parameters
    ----------
    N : int
        判定する上限
    """

    table = [True] * (N+1)
    table[0], table[1] = False, False

    for p in range(2, N+1):
        if not table[p]:
            continue
        q = p * 2
        while q <= N:
            table[q] = False
            q += p
    return table

def calc_divisors(N):
    """
    約数列挙

    Parameters
    ----------
    N : int
        判定する整数
    """

    ans = []
    for i in range(1, N+1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        ans.append(i)
        if N // i != i:
            ans.append(N // i)
    ans.sort()
    return ans

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

def GCD(A, B):
    """
    最大公約数
    """
    if B == 0: return A
    else: return GCD(B, A%B)

def LCM(A, B, G):
    """
    最小公倍数

    Parameters
    ----------
    A : int
        整数A
    B : int
        整数B
    G : int
        A, Bの最大公約数
    """
    return (A * B) // G