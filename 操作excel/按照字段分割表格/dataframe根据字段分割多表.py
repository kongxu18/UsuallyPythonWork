import pandas as pd

pd.set_option('display.max_rows', 15)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

# 读取excel
df = pd.read_excel('t3.xlsx')


df['type'] = df.iloc[:, 0].str.extract(r'^(.{2}).*')
df['name'] = df.iloc[:, 1].str.extract(r'\D*(\d*)-.*')
df['name2'] = df.iloc[:, 1].str.extract(r'(.*?)-.*')

dg = df.groupby('type')
writer = pd.ExcelWriter('G4_out.xlsx',mode='w')
sheet_name = 'G4_'
for key, df in dg:

    for _, dataframe in df.groupby('name'):


        sheet_name += dataframe.iloc[0, -1]
        sheet_name += dataframe.iloc[0, -3]

        dataframe = dataframe.iloc[:, :-3]
        dataframe = dataframe.reset_index(drop=True)
        dataframe = dataframe.round({'面积':2})

        dataframe.index = dataframe.index+1
        sum_ = dataframe.loc[:,'面积'].sum()
        # dataframe.iloc[:, 0].index.max()
        dataframe.loc[dataframe.iloc[:, 0].index.max()+1,'面积'] = sum_
        dataframe.loc[dataframe.iloc[:, 0].index.max(), '类别'] = '合计'
        dataframe.to_excel(writer, sheet_name=sheet_name, index=True, startrow=0, index_label='序号')
        print(dataframe)
        # print(sheet_name)
        sheet_name = 'G4_'



writer.save()
# print(dg)
# print(df)
