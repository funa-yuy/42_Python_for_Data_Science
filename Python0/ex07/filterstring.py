#
# 内包表記とlambaを使ってみる。(lambda 引数: 式)(引数)
#

import sys


def main():
    """S に含まれる単語のうち、長さが N を超える単語のリストを出力する

    プログラム実行時の第2引数をS、第3引数をNとし、
    S に含まれる単語のうち、長さが N を超える単語のリストを出力する
    """
    args = sys.argv
    try:
        # 引数のチェック
        assert len(args) == 3, "the arguments are bad"

        # 特殊文字（句読点や不可視文字など）がないかチェック
        invalid = [c for c in args[1] if not (c.isalnum() or c == ' ')]
        assert not invalid, "the arguments are bad"
        s = args[1].split()

        # 第２引数が数字かチェック
        assert args[2].isdecimal(), "the arguments are bad"
        n = int(args[2])

        # S に含まれる単語のうち、長さが N を超える単語のリストを出力
        res = [w for w in s if (lambda word: len(word) >= n)(w)]
        print(list(res))
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
