import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())

G = [set() for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    G[a - 1].add(b)
    G[b - 1].add(a)

for g in G:
    ANS = []
    ANS.append(len(g))
    ANS.extend(sorted(g))
    print(*ANS)

# Memo
# 最初[set()] * Nと書いてしまっていた
# 上の初期化だとsetが全て同じオブジェクトになってappendとかが全ての要素に適用されてしまう
# 二次元配列の場合はリスト内包表記を使うこと
