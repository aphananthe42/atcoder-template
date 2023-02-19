import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    setA = set(A)
    ANS = 0
    for i in range(K):
        if i in setA:
            ANS = i + 1
        else:
            print(i)
            exit()
    print(ANS)


if __name__ == "__main__":
    main()
