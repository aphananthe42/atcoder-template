import sys


def input():
    return sys.stdin.readline()[:-1]


T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a % 2 == 1:
            ans += 1
    print(ans)

# -------------------------------------

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Aodd = [a for a in A if a % 2 == 1]
    print(len(Aodd))

# Memo
# テストケースが複数ある問題形式に戸惑ってよく分からないところで時間を使ってしまった
# 下の書き方の方がスマート
