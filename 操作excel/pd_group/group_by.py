import pandas as pd

pd.set_option('display.max_columns', 30)


def group_by(df, writer):
    name = df['名称'].str.extract(r'(.*?)-.*')
    df['name'] = name
    group = df.groupby('name')
    for key, value in group:
        df = value.reset_index(drop=True)
        df.index = df.index + 1
        df.loc['合计', '面积(sqm)'] = df['面积(sqm)'].sum(axis=0)

        df.to_excel(writer, sheet_name=str(key), index=True, startrow=1, index_label='kaixin')
        writer.save()
        print(key, '--', df)


workbook = pd.ExcelFile('膜片铺平信息_0428.xlsx')
sheet_names = workbook.sheet_names
for i in range(len(sheet_names)):
    df = workbook.parse(sheet_name=sheet_names[i])
    writer = pd.ExcelWriter(sheet_names[i] + '.xlsx')
    group_by(df, writer)




