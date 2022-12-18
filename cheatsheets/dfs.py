"""
深さ優先探索(DFS)基本実装
"""

import sys


# 再帰関数のスタックオーバーフローを防ぐ
sys.setrecursionlimit(10 ** 8)

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
P = list(map(int, input().split()))

# 各頂点の子頂点リストを作る
chs = [[] for _ in range(N)]
for v in range(1, N):
    p = P[v-1]
    chs[p].append(v)

def dfs_standard(v, chs):
    """
    頂点vを根とする部分木を探索する再帰関数

    Parameters
    ----------
    v : int
        頂点v
    chs : list
        頂点vの子頂点のリスト
    """

    print(v, end=' ')
    for ch in chs[v]:
        dfs_standard(ch, chs)

depth = [0] * N
def dfs_depth(v, p, depth, chs):
    """
    頂点vを根とする部分木の深さを探索

    Parameters
    ----------
    v : int
        頂点v
    p : int
        頂点vの親
    depth : list
        頂点vの深さリスト
    chs : list
        頂点vの子頂点のリスト
    """

    if v == 0:
        depth[v] = 0
    else:
        depth[v] = depth[p] + 1

    for ch in chs[v]:
        dfs_depth(ch, v, depth, chs)

size = [0] * N
def dfs_size(v, p, size, chs):
    """
    頂点vを根とする部分木の頂点のサイズを探索

    Parameters
    ----------
    v : int
        頂点v
    p : int
        頂点vの親
    size : list
        頂点vを根とする部分木のサイズリスト
    chs : list
        頂点vの子頂点のリスト
    """

    for ch in chs[v]:
        dfs_size(ch, v, size, chs)
    
    size[v] = 1
    for ch in chs[v]:
        size[v] += size[ch]