"""
excel 排序
"""
import numpy as np
import pandas as pd
import re

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

sheets = pd.read_excel('板材清单表.xlsx', header=None, sheet_name=None)


# 对名字处理
def spilt(name):
    pattern = re.compile(r'/(\d+)([LR]{1})(\d+)[A-W](\d+)$')
    res = pattern.findall(name)[0]
    zhou = int(res[0])
    direct = res[1]
    tiao = int(res[2])
    lingjian = int(res[3])
    return zhou,direct,tiao,lingjian




spilt('G2/22L6V1')

data = []
for srcSheetName in sheets:
    print(srcSheetName)

    df = sheets.get(srcSheetName)
    print(df[0][481],type(df[0][481]))
    _, c = df.shape
    print(df.shape)
    src = df[0]
    for i in range(1, c):
        newdf = pd.concat([src, df[i]], axis=0, ignore_index=True)
        src = newdf
    print(newdf[newdf.isnull()].index)

    newdf = newdf.drop(newdf[newdf.isnull()].index,axis=0)
    newdf = newdf.reset_index(drop=True)

    newdf = pd.DataFrame(newdf)
    newdf['zhou'] = newdf[0].str.extract(r'/(\d+)[LR]{1}\d+[A-W]\d+$').astype('int')
    newdf['direct'] = newdf[0].str.extract(r'/\d+([LR]{1})\d+[A-W]\d+$')
    newdf['tiao'] = newdf[0].str.extract(r'/\d+[LR]{1}(\d+)[A-W]\d+$').astype('int')
    newdf['lingjian'] = newdf[0].str.extract(r'/\d+[LR]{1}\d+[A-W](\d+$)').astype('int')

    # 排序
    newdf = newdf.sort_values(by=['zhou', 'direct', 'tiao', 'lingjian'])

    # 分组成新列
    data_group = newdf.groupby('zhou')
    df = pd.DataFrame()
    for key, value in data_group:
        value = value.reset_index(drop=True)
        df_ = pd.concat([df,value[0]],axis=1,ignore_index=False)
        df = df_

    df = df.reset_index(drop=True)
    data.append([df,srcSheetName])

print(data)
writer = pd.ExcelWriter('tt.xlsx')
for item in data:
    item[0].to_excel(writer, sheet_name=item[1],header=None)
    writer.save()

writer.close()


