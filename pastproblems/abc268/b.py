import sys


def input():
    return sys.stdin.readline()[:-1]


S = input()
T = input()

if len(S) > len(T):
    print("No")
    exit()

isANS = True
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        isANS = False
        break

if isANS:
    print("Yes")
else:
    print("No")

# Memo
# スライスだともっと楽でスマートにできた...
# head = T[:len(S)]
# print('Yes') if S==head else print('No')
# 文字列メソッドstartswith()でも楽にできる
# print('Yes') if T.startswith(S) else print('No')
