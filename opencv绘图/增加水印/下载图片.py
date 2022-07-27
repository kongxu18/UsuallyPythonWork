import requests
import pymssql as mssql



def main():
    # sql
    serverName = 'erp.highbird.cn:9155'
    # 登陆用户名和密码
    userName = 'nizihua'
    passWord = '333333'
    # 建立连接并获取cursor
    conn = mssql.connect(serverName, userName, passWord, "base1", 'utf8')
    cursor = conn.cursor()
    sql = "select 员工登记姓名 as 拍照员工,t1.上次上传时间 as 拍照时间,文件路径,中文全称缓存 as 部位编号,参数值,复核值," \
          "cast(复核值 - 参数值 as decimal(10,2)) as 偏差值 from T254D参数上传数据 " \
          "inner join T254D全局部位记录 as t2 on t2.全局部位记录代码 = T254D参数上传数据.全局部位记录代码 " \
          "cross apply FTB00E文件信息(复测文件代码1) as t1 " \
          "inner join T100A员工登记姓名 on T100A员工登记姓名.员工登记姓名代码 = t1.创建用户 " \
          "where 复测文件代码1 >0  and 终止状态=0 and 复核值>0"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        path_list = [val[2] for val in data]
        print(path_list)

if __name__ == '__main__':
    main()