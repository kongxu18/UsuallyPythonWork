"""
分组只要头尾
"""
import pandas as  pd

pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)


class DealExcel(object):
    def __init__(self, path):
        self.path = path
        self.sheets = pd.read_excel('天窗纵向铝条  13#铝-材料表.xlsx', sheet_name=None)

    def cut_name(self):
        if self.path:
            for srcSheetName in self.sheets:
                print(srcSheetName, '------')
                df = self.sheets.get(srcSheetName)
                print(df)
                # df['zhouhao'] = df['zhou'] = newdf[0].str.extract(r'/(\d+)[LR]{1}\d+[A-W]\d+$').astype('int')


d = DealExcel('天窗纵向铝条  13#铝-材料表.xlsx')
d.cut_name()
