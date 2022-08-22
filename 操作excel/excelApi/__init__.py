import pandas as pd
from .style import *
from .data import SqlData

pd.set_option('display.max_columns', 1000)  # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.width', 1000)  # 显示最大的行宽
pd.set_option('display.max_colwidth', 1000)  # 显示最大的列宽

__version__ = '1.0.0'
__all__ = [
    'data'
]


def data_from_sql(sql: str):
    """
    传入 sql ，返回dataframe
    """
    df = SqlData(sql).data
    return df


def create_excel(filepath):
    ...