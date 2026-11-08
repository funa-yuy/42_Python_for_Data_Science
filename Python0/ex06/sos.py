#
# 辞書型を学ぶ。
#

import sys


def main():
    """引数をモールス信号に変換し、出力する

    プログラム実行時の第2引数をモールス信号に変換し、標準出力する。
    英数字と空白以外は未対応。
    """
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
    }
    args = sys.argv
    try:
        # 引数チェック
        assert len(args) == 2, "the arguments are bad"
        assert all(c.isalnum() or c == ' ' for c in args[1]), "the arguments are bad"

        # モールス信号に変換し、出力
        res = [NESTED_MORSE[c] for c in args[1].upper()]
        print(" ".join(res))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
