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


def main():
    """tests count_in_list
    """
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
    print(count_in_list(["toto", "tata", "toto"], ""))  # output: 0

    print(count_in_list([1, 1, 1], 1))  # output: 3
    print(count_in_list([], 1))  # output: 0

    print(count_in_list(["1"], "1"))  # output: 1
    print(count_in_list(["1"], 1))  # output: 0
    print(count_in_list([1], "1"))  # output: 0

    print(count_in_list(None, 1))  # output: AssertionError


if __name__ == "__main__":
    main()
