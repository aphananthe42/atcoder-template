import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N = int(input())
    A = input()

    ANS = A.replace("na", "nya")
    print(ANS)


if __name__ == "__main__":
    main()
