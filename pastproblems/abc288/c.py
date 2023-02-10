import sys
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def input():
    return sys.stdin.readline()[:-1]


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    ANS = 0
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
        else:
            ANS += 1
    print(ANS)


if __name__ == "__main__":
    main()

# Memo
# 閉路になる条件: 要素1と要素2の親が同じだったら、その要素同士を繋ぐと閉路になる
# 最初に辺が0だとして、入力値をUnionFindでunionしていく
# それぞれの要素同士が異なるものだったら、閉路にならないのでunionする
# それぞれの要素同士が同じものだったら、そこを繋ぐと閉路になってしまうのでANS+=1する
