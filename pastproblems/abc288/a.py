import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N = int(input())
    for i in range(N):
        a, b = map(int, input().split())
        print(a + b)


if __name__ == "__main__":
    main()
