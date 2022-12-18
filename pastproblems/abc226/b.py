import sys


def input():
    return sys.stdin.readline()[:-1]

N = int(input())
L = set()
for _ in range(N):
    l, *a = map(int, input().split())
    L.add(tuple(a))

print(len(L))

# Memo
# -> listの最初だけいらないみたいなケースでは上のようにアンパックすれば良い
# -> Setにmutableなオブジェクトを入れられないのでimmutableなtupleに変換している
# -> 重複抜きの個数を知りたいときはまずSetが使えるか考えること