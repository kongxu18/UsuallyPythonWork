import pymssql
import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, Border, Side, Alignment, PatternFill, colors
from openpyxl.utils import get_column_letter, column_index_from_string

pd.set_option('display.max_columns', 1000)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.width', 1000)  # 显示最大的行宽
pd.set_option('display.max_colwidth', 1000)  # 显示最大的列宽

border_style = Border(left=Side(border_style='thin', color='000000'),
                      right=Side(border_style='thin', color='000000'),
                      top=Side(border_style='thin', color='000000'),
                      bottom=Side(border_style='thin', color='000000'))

border_style2 = Border(left=Side(border_style='thin', color='000000'),
                       right=Side(border_style='thin', color='000000'),
                       top=Side(border_style='thin', color='000000'),
                       bottom=Side(border_style='thin', color='000000'),
                       diagonal=Side(border_style='thin', color='000000'),
                       diagonalUp=False, diagonalDown=True)

alignment_center = Alignment(horizontal='center', vertical='center', wrapText=True)
alignment_left = Alignment(horizontal='left', vertical='center', wrapText=True)
alignment_justify = Alignment(horizontal='justify', vertical='justify', wrap_text=True)
fill_red = PatternFill(fill_type="solid", fgColor="EE292B")
fill_green = PatternFill(fill_type="solid", fgColor="7FCA40")
fill_yellow = PatternFill(fill_type="solid", fgColor='EAC121')
fill_gray = PatternFill(fill_type="solid", fgColor='A6A6A6')
fill_blue = PatternFill(fill_type="solid", fgColor='8DB4E2')


def connection(sql):
    # 创建连接对象
    conn = pymssql.connect(host='erp.highbird.cn', server='erp.highbird.cn', port='9155', user='nizihua',
                           password='13o84x',
                           database='base1')

    cursor = conn.cursor(as_dict=True)

    cursor.execute(sql)
    # 列名
    columns = [name[0] for name in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    length = df.shape[0]
    print(length)
    return df


def set_style(cell, size=12):
    cell.font = Font(name='宋体', bold=True, size=size)
    cell.border = border_style
    # cell.quotePrefix = False
    cell.alignment = alignment_center
    # cell.fill = fill_blue


def A1(sheet):
    cell = sheet.cell(row=1, column=1)
    cell.value = '        柱行    '
    cell.border = border_style2
    cell.font = Font(name='宋体', bold=False, size=14)
    cell.alignment = alignment_justify


def excel(df: pd.DataFrame, save_name):
    ROWS = set()
    COLS = set()
    # df = df.sort_values(by=['行号'],axis=0,ascending=False)
    wb = Workbook()
    sheet = wb.active
    sheet.column_dimensions['A'].width = 14
    sheet.row_dimensions[1].height = 30

    # 设置a1 的样式
    A1(sheet)

    diff_min_col = df.loc[:, '一级序号'].min()

    # 最大行数
    max_row = df.loc[:, '二级序号'].max()
    print(max_row, 'row')
    # 醉倒列数
    max_col = df.loc[:, '一级序号'].max()

    col_index = 0

    # 对整个表样式进行添加边框
    # 获取表的规格
    excel_w = 0
    excel_h = 0

    for col in range(1, max_col + 2):

        for row in range(1, max_row + 2):

            if col == 1 and row == 1:
                ...
            else:
                if diff_min_col == 1:
                    cell = sheet.cell(row=row, column=col)
                    cell.border = border_style
                else:
                    if col <= max_col:
                        cell = sheet.cell(row=row, column=col)
                        cell.border = border_style

            # 针对偏移确定 excel 坐标

            val_series = df[(df['一级序号'] == col) & (df['二级序号'] == row)].loc[:, '构件全称缓存']
            # print(type(val),val)
            val = list(val_series)
            if len(val):
                val = val[0]
                col_index += 1
                # 设置列名
                if col not in COLS:
                    column_name = sheet.cell(row=1, column=col + 2 - diff_min_col, value='A' + str(col))
                    letter = get_column_letter(col + 2 - diff_min_col)
                    sheet.column_dimensions[letter].width = 27
                    set_style(column_name, 13)
                    COLS.add(col)

                    # cell = sheet.cell(row=row, column=col)
                    # cell.value = val
    print(col_index)
    # for index, row in df.iterrows():
    #     # 行列对应的坐标
    #     col_num = row['一级序号']
    #     row_num = row['二级序号']
    #     val = row['构件完整编号']
    #
    #     if col_num not in COLS:
    #         col_index += 1
    #         # 列 行
    #         cell_col = sheet.cell(row=1, column=col_index + 1, value='A' + str(col_num))
    #         letter = get_column_letter(col_index + 1)
    #         sheet.column_dimensions[letter].width = 27
    #         sheet.column_dimensions['A'].width = 14
    #         sheet.row_dimensions[1].height = 30
    #         set_style(cell_col, 13)
    #         COLS.add(col_num)
    #
    #     cell = sheet.cell(row=max_row + 1 - row_num, column=col_index + 1)
    #     if not cell.value:
    #         cell.value = val + '/' + str(design_len + 138) + '(' + str(design_len) + ')'
    #         set_style(cell)
    #
    #     if row_num not in ROWS:
    #         cell_row = sheet.cell(row=max_row + 1 - row_num, column=1, value=row_num)
    #         sheet.row_dimensions[max_row + 1 - row_num].height = 25
    #         set_style(cell_row, 13)
    #         ROWS.add(row_num)

    wb.save('%s.xlsx' % save_name)


if __name__ == '__main__':
    arg = 'K', 1
    sql = "select * from [FT254E按材料状态速查]('%s',%d) where 构件生存状态代码 > 1 order by 全局代码,部位代码,方位名称,一级序号,二级序号" % arg
    df = connection(sql)
    # print(df)
    # print(df.loc[:,'构件全称缓存'])
    excel(df, 'test')
