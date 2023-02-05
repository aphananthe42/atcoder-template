import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]

    ranker = S[:K]
    ranker.sort()
    for i in ranker:
        print(i)


if __name__ == "__main__":
    main()
