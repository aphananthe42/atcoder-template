import sys


def input():
    return sys.stdin.readline()[:-1]

A, B = map(int, input().split())

print(pow(A, B))