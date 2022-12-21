import sys


def input():
    return sys.stdin.readline()[:-1]

S = input()

if len(S) == 8:
    isNum = int(S[1:7].zfill(6)) > 99999
    if S[0].isupper and S[7].isupper:
        if isNum:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')