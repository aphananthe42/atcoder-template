import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N, M = map(int, input().split())

    if N % 2 == 0:
        if M <= N // 2:
            print("Yes")
        else:
            print("No")
    else:
        if M <= N // 2 + 1:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
