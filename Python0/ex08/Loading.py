#
# yeildを学ぶ。　ついでに、pythonの三項演算子も学ぶ。
#

import shutil


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
        size = shutil.get_terminal_size()
        columns = size[0]
        columns -= 35 + (len(str(total)) * 2)
        col_ratio = round(columns / total * num)
        bar = ["█" if i < col_ratio else " " for i in range(columns)]

        # 出力
        print(f"\r{str(ratio).rjust(3)}%|{''.join(bar)}| {num}/{total}", end="")
        yield x  # ここでxの値を保持したまま一時停止
        # ここから再開する
