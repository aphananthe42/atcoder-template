import sys


def input():
    return sys.stdin.readline()[:-1]

N = int(input())
first = []
second = []
setS = set()
for i in range(N):
    s = input()
    first.append(s[0])
    second.append(s[1])
    setS.add(s)

for j in first:
    if not j in ['H', 'D', 'C', 'S']:
        print('No')
        exit()

for k in second:
    if not k in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
        print('No')
        exit()

if len(setS) != N:
    print('No')
    exit()

print('Yes')

# Memo
# or, andを含む条件文で時間がかかった
# 最初 if (not j == 'H') or (not j=='D') or (not j=='C') or (not j=='S')でやろうとしていたが個別にやると絶対Noに入るのでダメ
# 実装方針, 解き方はすぐに理解できたのにPythonがよく分かっていなかった
# Filter文字列は別にlistじゃなくても普通に'HDCS'でよかった...

