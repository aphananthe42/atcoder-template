"""
幅優先探索(BFS)基本実装
"""

from collections import deque
import sys


def input():
    return sys.stdin.readline()[:-1]
################################################
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

dist = [-1] * N
dist[0] = 0
queue = deque([0])

def bfs_standard():
    """
    distに各頂点に到達するための最短手を格納する関数
    """

    while queue:
        v = queue.popleft()
        for next_v in G[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            queue.append(next_v)
################################################
# 四方向への移動を表すベクトル, 0: 下、1: 右、2: 上、3: 左
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

H, W = map(int, input().split())
X0, Y0, X1, Y1 = map(int, input().split())
S = [input() for _ in range(H)]

# 各マス (x, y) が何手目に探索されたかを格納するlist
dist = [[-1] * W for _ in range(H)]

queue = deque((0, 0))
# マス (X0, Y0) を始点とする
dist[0][0] = 0
queue.append((X0, Y0))

def bfs_maze():
    """
    迷路を幅優先探索し各マスへの最短経路を求める関数
    """

    while queue:
        x, y = queue.popleft()
        # マス (x, y) から 1 手で行けるマスを順に探索
        for dx, dy in zip(dxs, dys):
            # 隣接マス
            x2, y2 = x + dx, y + dy
            # マス (x2, y2) が盤面外である場合、黒マスである場合はスキップ
            if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W or S[x2][y2] == 'B': continue
            # マス (x2, y2) が探索済みであれば何もしない
            if dist[x2][y2] != -1: continue
            # マス (x2, y2) を探索する
            dist[x2][y2] = dist[x][y] + 1
            queue.append((x2, y2))
    # マス (X1, Y1) の値を答える
    print(dist[X1][Y1])


