import json
import sys
import io
import os
import shutil
import json
import pymssql
import pandas as pd
from openpyxl import Workbook, load_workbook
from 操作excel.excelApi.style import *


class SqlData(object):
    def __init__(self, sql):
        self.sql = sql
        self.__data = None
        self.__len = None
        self.connection()

    def connection(self):
        # 创建连接对象
        try:
            conn = pymssql.connect(host='erp.highbird.cn', server='erp.highbird.cn', port='9155', user='nizihua',
                                   password='13o84x',
                                   database='base1', charset='utf8')

            cursor = conn.cursor(as_dict=True)

            cursor.execute(self.sql)
            columns = [name[0] for name in cursor.description]
            df = pd.DataFrame(cursor.fetchall(), columns=columns)
            self.__len = df.shape[0]
            self.__data = df

        except Exception as err:
            raise ValueError('sql 交互出现问题：', str(err))

    @property
    def data(self):
        return self.__data

    @property
    def length(self):
        return self.__len


class DataDeal(object):
    def __init__(self, df):
        self.df = df
        self.set_df()

    def set_df(self):
        if isinstance(self.df, pd.DataFrame):
            if self.df.empty:
                raise ValueError('传入数据为空')
            else:
                self.column_type_revise()
                self.add_new_column()

    def column_type_revise(self):
        """
        对列的类型进行修正
        """
        self.df['工人工日'] = pd.to_numeric(self.df['工人工日'])
        self.df['劳务费小计'] = pd.to_numeric(self.df['劳务费小计'])

    def add_new_column(self):
        """
        拆分 日期增加 日子列
        """
        self.df['month'] = self.df['考勤日期'].astype('str').str.split('-').str.get(1).astype('int')

    def group_by_team(self):
        """
        按照班组统计
        """
        group: pd.DataFrame = self.df.groupby(['班组名称', 'month'])['劳务费小计'].sum().reset_index(name='sum')
        return group

    def sum_money_by_team(self):
        """
        按照班组统计所有金额
        """
        sum_money: pd.DataFrame = self.df.groupby(['班组名称'])['劳务费小计'].sum().reset_index(name='total')
        return sum_money

    def sum_money(self):
        """
        统计所有金额
        """
        sum_money: float = self.df['劳务费小计'].sum()
        return sum_money


def get_color():
    while True:
        yield fill_220
        yield fill_blue


def create_summary_sheet(wb, data_obj):
    ...


def create_model_sheets(wb, data_obj):
    group = data_obj.group_by_team()
    sum_money = data_obj.sum_money_by_team()
    total_money = data_obj.sum_money()

    sheet = wb.active
    sheet.title = '总汇'
    sheet.column_dimensions['A'].width = 14
    sheet.column_dimensions['B'].width = 10
    sheet.column_dimensions['C'].width = 20
    sheet.column_dimensions['D'].width = 20
    sheet.column_dimensions['E'].width = 20

    sheet.row_dimensions[1].height = 35
    sheet.row_dimensions[2].height = 30
    # 标题
    cell = sheet.cell(row=1, column=1, value='汇总表')
    cell.font = font16b
    cell.alignment = alignment_center
    sheet.merge_cells(start_row=1, end_row=1, start_column=1, end_column=4)

    # 列名
    column_name = ['班组', '月份', '金额', '总数']
    for i, name in enumerate(column_name):
        cell = sheet.cell(row=2, column=i + 1, value=name)
        cell.font = font14b
        cell.alignment = alignment_center

    # 主体
    tamp_team_name = None

    # 填充颜色
    color_fun = get_color()
    color = color_fun.__next__()
    for i, row in group.iterrows():

        name = row['班组名称']
        month = row['month']
        money = row['sum']
        all_money = sum_money[sum_money['班组名称'] == name].iloc[0, 1]

        values = [name, month, money, all_money]
        is_merge = False
        # 需要合并单元格
        if tamp_team_name == name:
            is_merge = True
        else:
            tamp_team_name = name
        # 针对不同班组间进行颜色填充
        if not is_merge:
            color = color_fun.__next__()
        for col, val in enumerate(values):
            now_row_index = 3 + int(str(i))
            cell = sheet.cell(row=now_row_index, column=col + 1, value=val)
            cell.fill = color
            cell.font = font12b
            cell.alignment = alignment_center
            cell.border = border_style
            sheet.row_dimensions[now_row_index].height = 30

            if col == 0 or col == 3:
                if is_merge:
                    sheet.merge_cells(start_row=now_row_index - 1, end_row=now_row_index, start_column=col + 1,
                                      end_column=col + 1)

    # 最右侧添加一个总计
    cell = sheet.cell(row=1, column=5, value='总劳务费')
    cell.font = font14b
    cell.fill = fill_blue
    cell.alignment = alignment_center
    cell.border = border_style

    cell = sheet.cell(row=2, column=5, value=total_money)
    cell.font = font14b
    cell.fill = fill_blue
    cell.alignment = alignment_center
    cell.border = border_style


def create_excel(df, save_path, model_path):
    wb = Workbook()
    data_obj = DataDeal(df)

    create_summary_sheet(wb, data_obj)
    create_model_sheets(wb, data_obj)
    wb.save(save_path)


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    argv = sys.argv
    argv = ['/Users/mac/Downloads/TridentSystem/scripts/python/creatExcel_template_xianchanglaowugz.py',
            'res.xlsx',
            't.json',
            '/Users/mac/Downloads/TridentSystem/filedata/exceltemplate/xianchanglaowugz.xlsx']

    excel_filePath = None
    json_filePath = None
    modelExcel_filePath = None
    if len(argv) > 1:
        try:
            excel_filePath = argv[1]
            json_filePath = argv[2]
            modelExcel_filePath = argv[3]
        except Exception as err:
            print('err:', '模板Excel生成参数不足')

    # 读取 excel json 文件
    if json_filePath:
        with open(json_filePath, encoding='utf8') as f:
            json_args: dict = json.loads(f.read())

            # 读取关键参数
            # 劳务公司代码
            companyCode = json_args.get('劳务公司代码')
            # 项目代码
            projectCode = json_args.get('项目代码')
            # 班组代码
            teamCode = json_args.get('班组代码')
            # 工人代码
            workerCode = json_args.get('工人代码')
            # 筛选时间
            startTime = json_args.get('起始时间')
            endTime = json_args.get('结束时间')

            print(projectCode, teamCode, workerCode, startTime, endTime)

    sql = "select  * from FT256D现场工人出勤统计('%s','%s','%s',%d,'%s','%s')" % (
        teamCode, companyCode, workerCode, projectCode, startTime, endTime)

    data: pd.DataFrame = SqlData(sql).data

    create_excel(data, excel_filePath, modelExcel_filePath)
