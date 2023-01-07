import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
L = []
for i in range(N):
    L.append(input())

for li in reversed(L):
    print(li)

# Memo
# reversedがパッと出てこなかったのでダメ
# L[::-1]でも逆順にみれる
