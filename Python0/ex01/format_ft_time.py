#
# フォーマット文字列を学ぶ
#
# フォーマット文字列(f文字列, f-string)とは
#   format()をより簡単に描けるようにしたもの。置き換えフィールド{}に値を挿入できる。
#


from datetime import datetime


dt = datetime.now()

dt_sec = dt.timestamp()  # timestamp()で、1970年1月1日0時0分0秒からの経過秒週を取得
print(f"Seconds since January 1, 1970:\
      {dt_sec} or {dt_sec:e} in scientific notation")

print(f"{dt:%b %d %Y}")  # %b 英語での月(3文字での省略),  %d 日, %Y 西暦(4桁)


"""
f文字列を使用せず、冗長に記述した場合


dt = datetime.now()

dt_sec = dt.timestamp()
dt_scientific_notation = "{:e}".format(dt_sec)
print("Seconds since January 1, 1970:",
    dt_sec, "or", dt_scientific_notation, "in scientific notation")

dt_str = dt.strftime("%b %d %Y")
print(dt_str)
"""
