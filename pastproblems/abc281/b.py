import sys


def input():
    return sys.stdin.readline()[:-1]

S = input()

if len(S) == 8:
    if not S[0].isnumeric():
        if not S[7].isnumeric():
            if S[1:7].isnumeric():
                if 100000<=int(S[1:7])<=999999:
                    print('Yes')
                    exit()
print('No')