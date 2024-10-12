#!/bin/bash
set -e


source ./venv/bin/activate


shopt -s nullglob
cur_dir=$(dirname "$(readlink -f "$0")")
tpl_dir="$cur_dir/databank"

tpl_py_files=("$tpl_dir"/*.tpl.py)
shopt -u nullglob

export PYTHONPATH="$cur_dir:$PYTHONPATH"
if [ ${#tpl_py_files[@]} -eq 0 ]; then
    echo "同一ディレクトリに .tpl.py ファイルが見つかりません。"
    exit 1
fi

for file in "${tpl_py_files[@]}"; do
    echo "実行中: $file"
    python "$file"
done
