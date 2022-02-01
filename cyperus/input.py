"""
基本入力リファレンス
"""

import sys


def input():
    """
    組込input()の速い版

    Returns
    -------
    sys.stdin.readline()[:-1] : str
    """

    return sys.stdin.readline()[:-1]

# 整数1つ
N = int(input())

# 整数複数個
N, K = map(int, input().split())

# 整数N個 (改行区切り)
L = [int(input()) for _ in range(N)]

# 整数N個 (スペース区切り)
A = list(map(int, input().split()))

# 二次元list
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 転置配列
R = list(zip(*A))

# タプルのlist
T = [tuple((input().split())) for _ in range(N)]

# 有向グラフ
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

# 無向グラフ
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)