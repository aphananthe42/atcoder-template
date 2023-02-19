import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ANS = 0
    for i in B:
        ANS += A[i - 1]
    print(ANS)


if __name__ == "__main__":
    main()
