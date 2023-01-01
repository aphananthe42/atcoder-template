from decimal import ROUND_HALF_UP, Decimal


def round_up(seed, place):
    """
    四捨五入(整数部分)

    Parameters
    ----------
    seed : int
        四捨五入する整数
    place : int
        四捨五入する位
    """
    place_str = f"1E{place}"
    X = Decimal(str(seed)).quantize(Decimal(place_str), rounding=ROUND_HALF_UP)
    return int(X)
