import sys


def input():
    return sys.stdin.readline()[:-1]


A, B, C, D, E, F = map(int, input().split())

DIVISOR = 998244353
Amod = A % DIVISOR
Bmod = B % DIVISOR
Cmod = C % DIVISOR
Dmod = D % DIVISOR
Emod = E % DIVISOR
Fmod = F % DIVISOR

print(((Amod * Bmod * Cmod) - (Dmod * Emod * Fmod)) % DIVISOR)

# Memo
# 桁数が多い数を考慮して計算前にmodを取った
# Pythonは整数のオーバーフローとか気にしなくていいので愚直に計算してもOKっぽい
