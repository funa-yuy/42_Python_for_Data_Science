#
# yieldを学ぶ
#


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        for item in iterable:
            if item:
                yield item  # ここでitemの値を保持したまま一時停止
                # ここから再開する
    else:
        for item in iterable:
            if function(item):
                yield item  # ここでitemの値を保持したまま一時停止
                # ここから再開する


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
    print(f"本家：{filter.__doc__}")
    print(f"自作：{ft_filter.__doc__}")

    numbers = range(7)

    print("=== 遅延評価（1つずつ判定・生成される様子）の検証 ===")
    print("本家：")
    orig_gen = filter(is_even, numbers)  # この段階では、ジェネレーターが作成されただけ
    print(f"{orig_gen}")
    for val in orig_gen:
        print(f"  -> : {val}")  # この時初めてyieldが呼び出される

    print("\n自作：")
    my_gen = ft_filter(is_even, numbers)  # この段階では、ジェネレーターが作成されただけ
    print(f"{my_gen}")
    for val in my_gen:
        print(f"  -> : {val}")  # この時初めてyieldが呼び出される

    print("\n=== next()で取り出すver ===")
    orig_gen = filter(is_even, numbers)
    my_gen = ft_filter(is_even, numbers)
    for i in range(3):  # rangeを３以上にするとエラー出る
        print(f"本家  -> : {next(orig_gen)}")
        print(f"自作  -> : {next(my_gen)}")

    print("\n=== list()で結果を確認するver ===")
    print(
        f"本家：{list(filter(is_even, numbers))}\n"
        f"自作：{list(ft_filter(is_even, numbers))}"
    )

    print("\n")

    print(
        f"本家：{list(filter(is_allTrue, numbers))}\n"
        f"自作：{list(ft_filter(is_allTrue, numbers))}"
    )

    print("\n")

    fruits = ["apple", "banana", "cherry", "date", "grape"]
    fruits_with_a = filter(lambda fruit: 'a' in fruit, fruits)
    ft_fruits_with_a = ft_filter(lambda fruit: 'a' in fruit, fruits)
    print(
        f"本家：{list(fruits_with_a)}\n"
        f"自作：{list(ft_fruits_with_a)}"
    )


if __name__ == "__main__":
    main()


# yieldを使わずに、ジェネレータ式で構成する方法。(ジェネレータ式は内部でyieldを使っている)
# def ft_filter(function, iterable):
#     """ft_filter(function or None, iterable) --> filter object

# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.
#     """
#     if function is None:
#         return (item for item in iterable if item)
#     return (item for item in iterable if function(item))
