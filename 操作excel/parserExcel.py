import pandas as pd


class Model_1_Excel:
    def __init__(self, argv):
        self.argv = argv
        self.data = None
        self.err = []
        try:
            self.sheets = pd.read_excel(str(self.argv), header=0, sheet_name=None)
        except Exception as e:
            self.err = [str(e)]

    def cut(self):
        if self.argv:
            try:
                for srcSheetName in self.sheets:
                    df = self.sheets.get(srcSheetName)
                    df['targetSheetName'] = None
                    self.columns_list = df.columns.values
                    self.sum_area_name = '面积(sqm)'
                    self.sum_area_name_index = 3
                    for i in range(len(self.columns_list)):
                        if '面积' in self.columns_list[i]:
                            self.sum_area_name = self.columns_list[i]

                        self.sum_area_name_index = i

                    print(self.columns_list)
                    type_s = df.iloc[:, 0]
                    name = df.iloc[:, 1]
                    color = df.iloc[:, 2]
                    area = df.iloc[:, 3]
                    perimeter = df.iloc[:, 4]

                    # 名称转换
                    name_key = name.str.split('-').str.get(0)
                    df['targetSheetName'] = name_key
                    MZS = name_key[name_key.str.contains("MZS")].index
                    MZT = name_key[name_key.str.contains("MZT")].index
                    MTT = name_key[name_key.str.contains("MTT")].index
                    MBC = name_key[name_key.str.contains("MBC")].index
                    MBF = name_key[name_key.str.contains("MBF")].index
                    MBT = name_key[name_key.str.contains("MBT")].index
                    MBX = name_key[name_key.str.contains("MBX")].index

                    df.iloc[MZS, -1] = df.iloc[MZS, -1].str.replace('MZS', 'MZ')
                    df.iloc[MZT, -1] = df.iloc[MZT, -1].str.replace('MZT', 'MZ')
                    df.iloc[MTT, -1] = df.iloc[MTT, -1].str.replace('MTT', 'MT')
                    df.iloc[MBC, -1] = df.iloc[MBC, -1].str.replace('MBC', 'MB')
                    df.iloc[MBF, -1] = df.iloc[MBF, -1].str.replace('MBF', 'MB')
                    df.iloc[MBT, -1] = df.iloc[MBT, -1].str.replace('MBT', 'MB')
                    df.iloc[MBX, -1] = df.iloc[MBX, -1].str.replace('MBX', 'MB')
                    # sheet 类别区分
                    df.iloc[:, -1] = srcSheetName + '_' + df['targetSheetName'] + df.iloc[:, 0].str[0:2]

                    self.data = df.groupby('targetSheetName')
                    # print(last_sum)
            except Exception as e:
                print(e)
                return None
        return True

    def cut_model_2(self):
        """
        G3/21L1
        区别在于数字
        一个数字一个表
        :return:
        """
        if self.argv:
            try:
                for srcSheetName in self.sheets:
                    print(srcSheetName)
                    df = self.sheets.get(srcSheetName)
                    columns_list = df.columns.values

                    df_left = df.iloc[:, :2]
                    df_left['l_name'] = df.iloc[:, 0].str.split('/').str.get(-1).str.split('L').str.join('')
                    df_right = df.iloc[:, 2:]
                    df_right['r_name'] = df.iloc[:, 2].str.split('/').str.get(-1).str.split('R').str.join('')

                    # print(type(df_left.iloc[0,-1]),df_left)
                    # print(df_right)

                    pd_all = pd.merge(df_left, df_right, how='left'
                                      , left_on='l_name',
                                      right_on='r_name')

                    data = pd_all.iloc[:, [0, 1, 2, 3, 4]].copy()
                    data.iloc[:, 2] = pd_all.iloc[:, 0].str.split('/').str.get(-1).str.split('L').str.get(0)
                    self.data = data.groupby('l_name')

            except Exception as e:
                self.err.append(str(e))
                return False
        return True

    def save_as(self, path):
        if not self.data:
            return None
        try:
            with pd.ExcelWriter(path) as writer:
                # for item in self.data:
                #     sheetName = item[0]
                #     df = item[1].reset_index(drop=True)
                #     df.to_excel(writer, sheet_name=sheetName)
                last_sum = self.data.agg({self.sum_area_name: 'sum'})
                for item in self.data:
                    sheetName = item[0]
                    df = item[1]
                    # print(sheetName)
                    sum_res = last_sum.loc[sheetName][0]
                    # print(sum_res,type(sum_res))
                    new_df = df.append({self.columns_list[0]: '求和', self.sum_area_name: sum_res}, ignore_index=True)
                    new_df = new_df.reset_index(drop=True)
                    new_df.index.name = '序号'
                    # print(df)
                    new_df.to_excel(writer, sheet_name=item[0])
        except Exception as e:
            print(e)
            return False
        return True

    def save_as_2(self, path):
        try:
            with pd.ExcelWriter(path) as writer:
                for item in self.data:
                    df = item[1]
                    new_df = df.iloc[:, [0, 1, 3, 4]]
                    new_df = new_df.reset_index(drop=True)
                    new_df.index.name = '序号'
                    new_df.to_excel(writer, sheet_name=item[0])
        except Exception as e:
            print(e,'========')
        return True

if __name__ == '__main__':
    pd.set_option('display.max_rows', 1000)
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.width', 500)
    argv = '水沟底板到檩条边距离G3.xlsx'
    p = Model_1_Excel(argv)
    p.cut_model_2()
    p.save_as_2('res222.xlsx')
