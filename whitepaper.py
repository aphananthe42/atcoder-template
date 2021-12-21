import sys


def input():
    return sys.stdin.readline()[:-1]

# 整数 1 つ
N = int(input())

# 整数複数個
N, K = map(int, input().split())

# 整数 N 個 (改行区切り)
L = [int(input()) for _ in range(N)]

# 整数 N 個 (スペース区切り)
A = list(map(int, input().split()))

# タプルのlist
T = [tuple((input().split())) for _ in range(N)]