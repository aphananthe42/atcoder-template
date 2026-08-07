"""
幅優先探索(BFS)基本実装
"""

import sys
from collections import deque


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

shortest_moves = [-1] * (N + 1)
shortest_moves[1] = 0

queue = deque()
queue.append(1)


def bfs():
    """
    shortest_movesに各頂点に到達するための最短手を記録する関数
    """
    while queue:
        pos = queue.popleft()
        for next in G[pos]:
            if shortest_moves[next] == -1:
                shortest_moves[next] = shortest_moves[pos] + 1
                queue.append(next)

    for i in range(1, N + 1):
        print(shortest_moves[i])
