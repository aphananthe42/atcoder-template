"""
めぐる式二分探索

初期値のok, ngを受け取り,is_okを満たす最小(最大)のokを返す
最大最小が逆の場合はよしなにひっくり返す
"""


def is_ok(arg):
    # 条件を満たすかどうか？を問題ごとに定義
    pass


def meguru_bisect(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
