# ft_package

This is a simple package.

The created package can be called from a script like the following:
```python
from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```

## install

1. ビルド
```bash

python3 -m pip install --upgrade build

# 配布物アーカイブを生成する
python3 -m build

# こうなるはず↓
# dist/
# ├── ft_package-0.0.1-py3-none-any.whl
# └── ft_package-0.0.1.tar.gz
```

2. インストール
```bash
# 以下のどちらでも実行可能
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

3. 確認
```bash
# 一覧に存在するか確認
pip list

# 詳細を表示
pip show -v ft_package"
```