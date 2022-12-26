import sys


def input():
    return sys.stdin.readline()[:-1]

S = input()

print(len(S) - S.count('00'))