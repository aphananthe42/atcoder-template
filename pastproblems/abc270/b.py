import sys


def input():
    return sys.stdin.readline()[:-1]

X, Y, Z = map(int, input().split())

if Y<X and Y<0:
    print(abs(X))
    exit()
elif X<Y and Y>0:
    print(abs(X))
    exit()

if 0<Y<Z or Z<Y<0:
    print(-1)
    exit()
else:
    ans = abs(Z)
    ans += abs(Z-Y)
    ans += abs(X-Y)
    print(ans)
    exit()

# Memo
# -> アルゴリズムとか関係ない、ただの場合分け
# -> 頭が思考停止して回答を見てしまったため、自力で解けるようになる必要がある
# -> 愚直に場合分けを考えるしかない


