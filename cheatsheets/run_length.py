from itertools import groupby


def runLengthEncode(S):
    """
    ランレングス圧縮(エンコード)

    Parameters
    ----------
    S: str
        圧縮前の文字列

    Returns
    -------
    list[tuple[str | int]]
        エンコードされたlist

    Examples
    --------
    "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
    """
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def runLengthDecode(L):
    """
    ランレングス圧縮(デコード)

    Parameters
    ----------
    L: list[tuple[str | int]]
        デコードするlist

    Returns
    -------
    str
        デコードされた文字列

    Examples
    --------
    [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
    """
    res = ""
    for c, n in L:
        res += c * int(n)
    return res


def runLengthEncodeToString(S):
    """
    ランレングス圧縮

    Parameters
    ----------
    S: str
        圧縮前の文字列

    Returns
    -------
    str
        圧縮後の文字列

    Examples
    --------
    "aabbbbaaca" -> "a2b4a2c1a1"
    """
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res
