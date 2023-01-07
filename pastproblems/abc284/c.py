import sys


def input():
    return sys.stdin.readline()[:-1]


# 頂点 v を始点とした深さ優先探索
def dfs(v, G, seen):
    # 頂点 v を探索済みにする
    seen[v] = True
    # G[v] に含まれる頂点 v2 について、
    for v2 in G[v]:
        # v2 がすでに探索済みならば、スキップする
        if seen[v2]:
            continue
        # v2 始点で深さ優先探索を行う (関数を再帰させる)
        dfs(v2, G, seen)
    return


# main
# 入力を受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト
for i in range(M):
    a, b = map(int, input().split())
    # 頂点 a から頂点 b への辺を隣接リストに入れる
    G[a - 1].append(b - 1)
    # 無向グラフのため、頂点 b から頂点 a への辺を隣接リストに入れる
    G[b - 1].append(a - 1)

seen = [False for _ in range(N)]  # seen[v]：頂点 v が探索済みなら true, そうでないなら false
ans = 0  # 答えとなる変数
# 全ての頂点について
for v in range(N):
    # 頂点 v がすでに訪問済みであれば、スキップ
    if seen[v]:
        continue
    # そうでなければ、頂点 v を含む連結成分は未探索
    # 深さ優先探索で新たに訪問し、答えを 1 増やす
    dfs(v, G, seen)
    ans += 1
# 答えを出力する
print(ans)

# Memo
# アルゴ式のコピペ...
# 求めたいものは何となく理解できたのでググれたがグラフやっていなさすぎてUnionFind木であることすら分かっていなかった
# UnionFind勉強しろ
