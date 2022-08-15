# # 对整个表样式进行添加边框
#     # 获取表的规格
#     excel_w = max_col+2-diff_min_col
#     # 应为下面再包含汇总
#     excel_h = max_row + 1
# for col in range(1, max_col + 2):
#
#     for row in range(1, max_row + 2):
#
#         if col == 1 and row == 1:
#             ...
#         else:
#             if diff_min_col == 1:
#                 cell = sheet.cell(row=row, column=col)
#                 cell.border = border_style
#             else:
#                 if col <= max_col:
#                     cell = sheet.cell(row=row, column=col)
#                     cell.border = border_style
#
#         # 针对偏移确定 excel 坐标
#
#         val_series = df[(df['一级序号'] == col) & (df['二级序号'] == row)].loc[:, '构件全称缓存']
#         # print(type(val),val)
#         val = list(val_series)
#         if len(val):
#             val = val[0]
#             col_index += 1
#             # 设置列名
#             if col not in COLS:
#                 column_name = sheet.cell(row=1, column=col + 2 - diff_min_col, value='A' + str(col))
#                 letter = get_column_letter(col + 2 - diff_min_col)
#                 sheet.column_dimensions[letter].width = 27
#                 set_style(column_name, 13)
#                 COLS.add(col)
#
#                 # cell = sheet.cell(row=row, column=col)
#                 # cell.value = val


import pandas as pd

df = pd.DataFrame(data=[[1,2,3],[1,2,1],[1,2,1],[2,2,2],[2,2,3],[3,4,5]],columns=['a','b','c'])
print(df)

d = df.groupby(['a','c']).agg({'c':'count'})
# for i,df in d:
#     print(i)
#     print(df)
print(d)

c = df.groupby(['a','c'])['c'].count().reset_index(name='count')
print(c)

