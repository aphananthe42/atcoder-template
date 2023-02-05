"""
深さ優先探索(DFS)関連ライブラリ
"""

import sys

# 再帰関数のスタックオーバーフローを防ぐ
sys.setrecursionlimit(10**8)


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)


def dfs(pos, graph, visited):
    """
    深さ優先探索を行う再帰関数

    Parameters
    ----------
    pos: int
        現在位置
    graph: list
        探索を行うグラフ
    visited: list
        訪問済みかどうかを記録するリスト
    """
    visited[pos] = True
    for next in graph[pos]:
        if not visited[next]:
            dfs(next, graph, visited)
