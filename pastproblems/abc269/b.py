import sys


def input():
    return sys.stdin.readline()[:-1]

S = [input() for _ in range(10)]

AB = []
CD = []
isFound = False
for indexAB, s in enumerate(S):
    if '#' in s:
        AB.append(indexAB+1)
        if not isFound:
            for indexCD, t in enumerate(s):
                if t == '#':
                    CD.append(indexCD+1)
            isFound = True

A = min(AB)
B = max(AB)
C = min(CD)
D = max(CD)

print(A, B)
print(C, D)

# Memo
# 入力で割と脳死でリスト内表記を書けたのはよかった
# isFoundなくても大して計算量に寄与しないのでなくていいがこの部分の無駄をどうすればいいかは分からない
# 実装自体は軽いが問題文を理解するのに時間がかかった... 
# 文字式とかめんどくさがらず飛ばさなければもう少し早くいけた気がする