#
# スライス法と、numpyライブラリの配列の型を学ぶ。
#

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """リスト形状を表示し、指定された開始値と終了値に基づいてスライスしたリストを返す。

    Args:
        family (list): 2次元配列のリスト
        start (int): 開始位置
        end (int): 終了位置

    Returns:
        list: スライスしたリスト
    """
    assert isinstance(family, list), "The first argument must be of type a list."

    # numpyライブラリで、listから配列を作る
    arr_family = np.array(family)
    arr_new_family = np.array(family[start:end])

    # 次元数が2でない場合、AssertionError
    assert arr_family.ndim == 2, "The first argument must be a two-dimensional array."

    # 形状を表示
    print(
        f"My shape is : {arr_family.shape}\n"
        f"My new shape is : {arr_new_family.shape}"
    )

    # printしたときに配列だと空白で区切られるため、listのスライス法を利用して返す
    return (family[start:end])


def run_test(case: str, family: list, start: int, end: int):
    """slice_me()を実行するテスト関数

    Args:
        case (str): テスト時に表示する文字列
        family (list): 2次元配列
        start (int): 開始値
        end (int): 終了値
    """
    print(f"=== {case} ===")
    print(slice_me(family, start, end))
    print()


def main():
    """tests slice_me
    """
    family = [
                [1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]
            ]
    run_test("(0, 2)", family, 0, 2)  # 正常
    run_test("(1, -2)", family, 1, -2)  # 内大→外小
    run_test("(1, -1)", family, 1, -1)  # 内大→外小
    run_test("(-2, 1)", family, -2, 1)  # 外小→内大
    run_test("(2, 5)", family, 2, 5)  # 内小→外大
    run_test("(-1, 4)", family, -1, 4)  # 外小→内大
    run_test("(4, 5)", family, 4, 5)  # 外小→外s大
    run_test("(0, 0)", family, 0, 0)  # 正常

    family2 = [1.80, 78.4, 2.15, 102.7]
    print(f"1次元配列 {family2=}--------------\n")
    run_test("(0, 2)", family2, 0, 2)

    family3 = []
    print("空のリスト {family3=}--------------\n")
    run_test("(0, 2)", family3, 0, 2)

    family4 = [
                [[1.80, 78.4], [2.15, 102.7]],
                [[2.10, 98.5], [1.88, 75.2]]
            ]
    print("3次元配列 {family4=}--------------\n")
    run_test("(0, 2)", family4, 0, 2)

    print("None --------------\n")
    run_test("listがNone", None, 0, 2)


if __name__ == "__main__":
    main()
