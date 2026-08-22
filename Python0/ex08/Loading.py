#
# yeildを学ぶ。　ついでに、pythonの三項演算子も学ぶ。
#

import os

from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    """tqdm()の再現

    プログレスバーを表示できるtqdm()を再現する関数。

    Args:
        lst (range): 進捗バーの全体範囲を指定するrangeオブジェクト。

    Yields:
        int: 現在の処理インデックス（0始まり）。（例: 3つ目の処理を実行中の場合は 2が返される）
    """
    # 範囲が0以下だったら、何もしない
    if len(list(lst)) <= 0:
        print("0it [00:00, ?it/s]")
        return

    total = (list(lst)[-1] + 1) - list(lst)[0]
    for x in range(0, total):
        num = x + 1
        ratio = round(num / total * 100)

        # ターミナルサイズをもとに、プログレスバーを作成
        size = os.get_terminal_size()
        columns = size[0]
        columns -= 35 + (len(str(total)) * 2)
        col_ratio = round(columns / total * num)
        bar = ["█" if i < col_ratio else " " for i in range(columns)]

        # 出力
        print(f"\r{str(ratio).rjust(3)}%|{''.join(bar)}| {num}/{total}", end="")
        yield x  # ここでxの値を保持したまま一時停止
        # ここから再開する


def run_test(case: str, rng: range) -> None:
    """同じ引数でft_tqdm()とtqdm()を実行するテスト用関数

    Args:
        case (str): テスト時に表示する文字列
        rng (range): 引数で与えるrange
    """
    print(f"======== {case} ========")
    for elem in ft_tqdm(rng):
        sleep(0.005)
    print()
    for elem in tqdm(rng):
        sleep(0.005)
    print()


def main():
    """tests ft_tqdm
    """
    test_cases = [
        ["普通 range(333)", range(333)],
        ["始まりと終わりを指定 range(0, 1)", range(0, 1)],
        ["途中で始まる range(10, 20)", range(10, 20)],
        ["始まりと終わりが同じ range(20, 20)", range(20, 20)],
        ["始まりの方が少ない 1 range(10, 20)", range(10, 20)],
        ["始まりの方が少ない 2 range(-10, 0)", range(-10, 0)]
    ]

    for test in test_cases:
        run_test(test[0], test[1])


if __name__ == "__main__":
    main()
