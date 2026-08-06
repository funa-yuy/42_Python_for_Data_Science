#
# assertを学ぶ。assertは、条件式が"false"の時に、AssertionErrorを発生させる。
#

import sys

# 引数の数をチェック
args = sys.argv
if len(args) == 1:
    sys.exit()

try:
    assert len(args) == 2, "more than one argument is provided"

    # 数値チェック
    val = args[1]
    tmp = val
    if len(val) > 1 and (val[0] == '-' or val[0] == '+'):
        tmp = val[1:]
    assert tmp.isdecimal(), "argument is not an integer"

    # 偶数・奇数チェック
    if int(val) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
