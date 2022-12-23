import sys
from itertools import combinations


def input():
    return sys.stdin.readline()[:-1]

H, W = map(int, input().split())
A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

for i1, i2 in combinations(range(H), 2):
    for j1, j2 in combinations(range(W), 2):
        print(i1, i2, j1, j2)
        if A[i1][j1]+A[i2][j2] <= A[i2][j1]+A[i1][j2]:
            continue
        else:
            print('No')
            exit()

print('Yes')

# Memo
# 以下のようにやってもちゃんとした2重ループになぜかならない...
# iteratorは変数に格納せずそのまま使うようにする
I = combinations(range(H), 2)
J = combinations(range(W), 2)
for i1, i2 in I:
    for j1, j2 in J:
        print(i1, i2, j1, j2)