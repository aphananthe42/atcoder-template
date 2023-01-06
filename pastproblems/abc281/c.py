import sys


def input():
    return sys.stdin.readline()[:-1]


N, T = map(int, input().split())
A = list(map(int, input().split()))

T %= sum(A)
for i in range(len(A)):
    if T - A[i] <= 0:
        print(i + 1, T)
        exit()
    else:
        T -= A[i]

# Memo
# 最初愚直にシミュレーションしてTLE -> Tが大きすぎるため
