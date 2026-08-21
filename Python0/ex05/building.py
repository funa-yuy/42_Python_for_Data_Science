#
# main関数や、標準入力のやり方を学ぶ。
#

import sys


def ispunctuation(c: str) -> bool:
    """文字列が記号であればTrueを、そうでなければFalseを返す。

    Args:
        c (str): 文字列

    Returns:
        bool: 文字列c内の全てが記号であればTrue、1文字でも記号以外があればFalseを返す。

    Warning:
        英語以外(日本語など)も記号として扱います。
    """
    if c.isupper() or c.islower() or c.isspace() or c.isdecimal():
        return False
    return True


def main():
    """大文字・小文字・記号・空白・数字の数を表示する

    プログラム実行時の第２引数、もしくは標準入力で文字列を受け取り、
    この文字数と、文字列内にある大文字・小文字・記号・空白・数字の数をそれぞれ表示する。
    """
    args = sys.argv
    assert len(args) <= 2, "more than one argument is provided"
    if len(args) == 1:
        print("What is the text to count?")
        input_text = sys.stdin.read()
    else:
        input_text = args[1]

    num_upper = sum(c.isupper() for c in input_text)
    num_lower = sum(c.islower() for c in input_text)
    num_punctuation = sum(ispunctuation(c) for c in input_text)
    num_space = sum(c.isspace() for c in input_text)
    num_digit = sum(c.isdecimal() for c in input_text)

    print(f"The text contains {len(input_text)} characters:")
    print(f"{num_upper} upper letters")
    print(f"{num_lower} lower letters")
    print(f"{num_punctuation} punctuation marks")
    print(f"{num_space} spaces")
    print(f"{num_digit} digits")


if __name__ == "__main__":
    main()
