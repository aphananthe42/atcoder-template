import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
C = [0] * (N + 1)

for i in range(N - 1):
    a, b = map(int, input().split())
    C[a] += 1
    C[b] += 1

if (N - 1) in C:
    print("Yes")
else:
    print("No")

# Memo
# なぜか有向グラフ的に考えていて詰まっていた
# 無向グラフなのでメモlistの両頂点に辺を記録する
# "Starである"とは(頂点の数-1)個の辺を持つ点を探せばいいので、例えば頂点5個だったら4つの辺を持つ点を探せば良い
