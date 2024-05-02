import csv
import os
import sys

from pathlib import Path

from pprint import pprint

def define_env(env):
    @env.macro
    def csv2table(path_csv):
        # 相対パスで指定したcsvからtableを生成するマクロ
        # 1行目で記入されない項目については表示しない
        dir_current = Path(env.variables.page.file.abs_src_path).parent
        path_file = os.path.join(dir_current, path_csv)

        ## csv file -> markdown table
        with open(path_file, encoding='utf8', newline='') as f:
            def row2text(row):
                return '| '  + ' | '.join(row) + ' |'
            csvreader = [i for i in csv.reader(f)]
            cols = len(csvreader[0])
            split_row = row2text(['-' for i in range(cols)])
            table_rows = [row2text(row) for row in csvreader]
        table_rows.insert(1, split_row)
        return '\n'.join(table_rows)
