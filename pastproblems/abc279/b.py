import sys


def input():
    return sys.stdin.readline()[:-1]


S = input()
T = input()

if T in S:
    print("Yes")
else:
    print("No")
