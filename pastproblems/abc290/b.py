import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N, K = map(int, input().split())
    S = input()

    ANS = ""
    counter = 0
    for i in S:
        if counter == K:
            ANS += "x"
        else:
            if i == "o":
                counter += 1
                ANS += "o"
            else:
                ANS += "x"
    print(ANS)


if __name__ == "__main__":
    main()
