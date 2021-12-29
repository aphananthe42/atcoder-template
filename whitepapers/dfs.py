import sys


###深さ優先探索(DFS)基本実装###
# 再帰関数のスタックオーバーフローを防ぐ
sys.setrecursionlimit(10 ** 8)

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
P = list(map(int, input().split()))

#  頂点vを根とする部分木を探索する再帰関数
def rec(v, chs):
    print(v, end=' ')
    for ch in chs[v]:
        rec(ch, chs)

# 各頂点の子頂点リストを作る
chs = [[] for _ in range(N)]
for v in range(1, N):
    p = P[v-1]
    chs[p].append(v)

rec(0, chs)