import pandas as pd


class ResetId(object):
    def __init__(self, path):
        self.path = path

    def read(self, step):
        df = pd.read_excel(self.path)
        print(df.shape)
        col_length = df.shape[1]
        new_df = pd.DataFrame()
        if step:
            cursor = 0
            for num in range(0, col_length + 1, step):
                if num:
                    print(cursor, num)
                    temp_df = df.iloc[:, cursor:num]
                    temp_df.columns = ['T1', 'T2', 'T3', 'T4']
                    temp_df = temp_df.drop(temp_df[temp_df['T1'].isnull()].index, axis=0)

                    cursor = num
                    new_df = pd.concat([new_df, temp_df], axis=0,ignore_index=True)

            new_df = new_df.sort_values(by=['T1'], ascending=True,ignore_index=True)
            new_df.to_excel('ttt.xlsx',index=None)
            print(new_df)

        # df1 = df.iloc[:10, 0:4]
        # df1.columns = [0,1,2,3]
        # df2 = df.iloc[:10, 4:8]
        # df2.columns = [0, 1, 2, 3]
        # df3 = pd.concat([df1, df2], axis=0)
        # print(df3)


one = ResetId('图纸节点坐标.xlsx', )
one.read(4)
