def alpha_to_num(alpha):
    """
    アルファベット->整数の変換関数

    Parameters
    ----------
    alpha: str
        変換するA~Z文字列: ABX, ABGS, Zなど

    Returns
    -------
    num: int
        変換後の整数
    """
    num = 0
    for index, item in enumerate(list(alpha)):
        num += pow(26, len(alpha) - index - 1) * (ord(item) - ord("A") + 1)
    return num


def num_to_alpha(num):
    """
    整数->アルファベットの変換関数

    Parameters
    ----------
    num: int
        変換する整数

    Returns
    -------
    char(64 + num): str
        変換後の文字列
    """
    if num <= 26:
        return chr(64 + num)
    elif num % 26 == 0:
        return num_to_alpha(num // 26 - 1) + chr(90)
    else:
        return num_to_alpha(num // 26) + chr(64 + num % 26)
