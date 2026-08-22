#
# 内包表記を学ぶ。 [ 出力する値  for  要素  in  イテラブル  if  条件式 ]
#


def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def is_even(n: int) -> bool:
    """指定された整数が偶数かどうかを判定する

    Args:
        n (int): 判定対象の整数。

    Returns:
        bool: 偶数の場合は True、奇数の場合は False。
    """
    return n % 2 == 0


def is_allTrue(_n: int) -> bool:
    """常にTrueを返す

    Args:
        _n (int): 任意の整数（内部処理では使用しない）。

    Returns:
        bool: 常にTrue。
    """
    return (True)


def main():
    """tests ft_filter.
    """
    print("__doc__：")
    print(f"自作{filter.__doc__}")
    print(f"本家：{ft_filter.__doc__}")

    numbers = [1, 2, 3, 4, 5, 6]
    print(
        f"本家：{filter(is_even, numbers)}, {list(filter(is_even, numbers))}\n"
        f"自作：{ft_filter(is_even, numbers)}, {list(ft_filter(is_even, numbers))}"
    )

    print("\n")

    numbers = [1, 2, 3, 4, 5, 6]
    print(
        f"本家：{filter(is_allTrue, numbers)}, {list(filter(is_allTrue, numbers))}\n"
        f"自作：{ft_filter(is_allTrue, numbers)}, {list(ft_filter(is_allTrue, numbers))}"
    )

    print("\n")

    fruits = ["apple", "banana", "cherry", "date", "grape"]
    fruits_with_a = filter(lambda fruit: 'a' in fruit, fruits)
    ft_fruits_with_a = ft_filter(lambda fruit: 'a' in fruit, fruits)
    print(
        f"本家：{fruits_with_a}, {list(fruits_with_a)}\n"
        f"自作：{ft_fruits_with_a}, {list(ft_fruits_with_a)}"
    )


if __name__ == "__main__":
    main()
