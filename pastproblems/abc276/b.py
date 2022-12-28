import sys


def input():
    return sys.stdin.readline()[:-1]

N, M = map(int, input().split())

G = [set() for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    G[a-1].add(b)
    G[b-1].add(a)

for g in G:
    ANS = []
    ANS.append(len(g))
    ANS.extend(sorted(g))
    print(*ANS)