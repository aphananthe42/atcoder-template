from collections import deque


def topological_sort(G, in_degrees):
    """
    トポロジカルソート

    Parameters
    ----------
    S: list[list[int]]
        有向グラフ
    in_degrees: list[int]
        各頂点の入次数のリスト

    Returns
    -------
    list[int]
        ソートされたグラフ
    """
    queue = deque()
    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            queue.append(i)

    ANS = []
    while queue:
        v = queue.popleft()
        ANS.append(v)
        for adj in G[v]:
            in_degrees[adj] -= 1
            if in_degrees[adj] == 0:
                queue.append(adj)
    return ANS
