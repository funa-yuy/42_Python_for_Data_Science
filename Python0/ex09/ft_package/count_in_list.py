def count_in_list(lst: list, val: any) -> int:
    """_summary_

    Args:
        lst (list): 検索元のリスト
        val (any): 検索対象の値

    Returns:
        int: lstのうち、valが登場する回数
    """
    assert isinstance(lst, list), "The first argument must be of type a list."
    return (lst.count(val))
