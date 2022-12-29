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
        if A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]:
            continue
        else:
            print("No")
            exit()

print("Yes")

# Memo
# 以下のようにやってもちゃんとした2重ループになぜかならない...
# iteratorは変数に格納せずそのまま使うようにする
i_comb = combinations(range(H), 2)
j_comb = combinations(range(W), 2)
for i1, i2 in i_comb:
    for j1, j2 in j_comb:
        print(i1, i2, j1, j2)
