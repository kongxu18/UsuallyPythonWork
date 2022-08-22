import json
import sys, io, os, shutil


if __name__ == '__main__':
    s = ['/Users/mac/Downloads/TridentSystem/scripts/python/creatExcel_template_xianchanglaowugz.py', '/Users/mac/Downloads/TridentSystem/filedata/excel/8bfbbf6e-b010-53df-dd00-fdc213d70e30.xlsx', '/Users/mac/Downloads/TridentSystem/filedata/exceljson/8bfbbf6e-b010-53df-dd00-fdc213d70e30.json', '/Users/mac/Downloads/TridentSystem/filedata/exceltemplate/xianchanglaowugz.xlsx'] ----python----------
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    argv = sys.argv

    print(argv)