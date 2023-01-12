import sys


def input():
    return sys.stdin.readline()[:-1]


A, B, C = map(int, input().split())

if A**2 + B**2 < C**2:
    print("Yes")
else:
    print("No")
