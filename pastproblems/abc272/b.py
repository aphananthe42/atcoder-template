import sys
from itertools import combinations


def input():
    return sys.stdin.readline()[:-1]

N, M = map(int, input().split())
L = [[False for _ in range(N)] for _ in range(N)]

for m in range(M):
    persons = list(map(int, input().split()))[1:]
    for c1, c2 in combinations(persons, 2):
        L[c1-1][c2-1] = True
        L[c2-1][c1-1] = True

   
for i in range(N):
    for j in range(N):
        if i == j: continue
        if L[i][j] == False:
            print('No')
            exit()

print('Yes')

# Memo
# combinations使うところは良かった
# dicで保存しようとしてTLEになった
# 各々のOn/Offを保存したいだけなら二重配列で十分