import pymssql
import pandas as pd


class Data(object):
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
            print(err)

    @property
    def data(self):
        return self.__data

    @property
    def length(self):
        return self.__len
