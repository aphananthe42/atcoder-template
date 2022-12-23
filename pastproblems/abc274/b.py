import sys


def input():
    return sys.stdin.readline()[:-1]

H, W = map(int, input().split())
G = []
for i in range(H):
    c = input()
    G.append(c)

ANS = [0] * W
for row in G:
    for dot in range(len(row)):
        if row[dot] == '#':
            ANS[dot] += 1

print(*ANS)

# Memo
# 特になし
# 実装しながら分かりやすい変数名を打てたらもう少し早く解けた