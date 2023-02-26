import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    X = int(input())

    dp = [False] * (X + 1)
    dp[0] = True

    rice_cake = [False] * (X + 1)
    for b in B:
        rice_cake[b] = True

    for i in range(1, X + 1):
        if not rice_cake[i]:
            for a in A:
                if i - a >= 0 and dp[i - a]:
                    dp[i] = True

    if dp[X]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
