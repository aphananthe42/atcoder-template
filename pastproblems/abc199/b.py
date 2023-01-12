import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ANS = min(B) - max(A) + 1
print(max(0, ANS))
