from os import getenv
import pymssql
import pandas as pd
import time

# 创建连接对象
conn = pymssql.connect(host='erp.highbird.cn', server='erp.highbird.cn', port='9155', user='nizihua', password='333333',
                       database='base1')

cursor = conn.cursor(as_dict=True)

df = pd.read_excel('邮寄信息--2021中秋.xlsx')
df['维护人'] = df['维护人'].ffill()
df['联系电话'] = df['联系电话'].ffill()
df['维护情况'] = df['维护情况'].ffill()

sql = 'select * from V113A名册员工全部 where 员工登记姓名 = %s'

for index, items in df.iterrows():
    # print(index,items,'---')

    维护人 = items['维护人']
    客户姓名 = items['客户姓名']
    邮寄地址 = items['邮寄地址']
    联系电话 = items['联系电话']
    维护情况 = items['维护情况']
    五百 = items[500]
    一千 = items[1000]
    两千 = items[2000]
    是否需要贺卡 = items['是否需要贺卡']
    备注 = items['备注']
    状态 = items.get('状态')
    print(items)

    cursor.execute(sql, 维护人)
    row = cursor.fetchone()

    print(row['员工登记姓名代码'], '---')
    维护人 = row['员工登记姓名代码']
    print(维护人, 客户姓名, 邮寄地址, 联系电话, 维护情况, 是否需要贺卡, 备注, 状态)
    说明 = '500的京东卡' + ',需要贺卡：' + 是否需要贺卡 + ',' + 备注 + ',' + 状态 if 状态=='nan' else ''
    if 一千:
        说明 = '1000的京东卡' + ',需要贺卡：' + 是否需要贺卡 + ',' + 备注 + ',' + 状态 if 状态=='nan' else ''
    elif 两千:
        说明 = '2000的京东卡' + ',需要贺卡：' + 是否需要贺卡 + ',' + 备注 + ',' + 状态 if 状态=='nan' else ''
    print(维护人, 客户姓名, 邮寄地址, 联系电话, 维护情况, 说明)
    sql2 = r"INSERT INTO [dbo].[T735C邮寄快递记录] ([考勤登记地点代码],[项目登记名称代码],[邮寄快递对象代码],[邮寄快递种类代码],[申请人员姓名代码],[邮寄内容名称],[要求寄送日期],[要求注意事项],[收件人的姓名],[邮寄数量说明],[收件单位名称],[收件人的手机],[收件人的地址],[收件人的邮编],[价值重要程度],[费用支付人员代码],[登记确认状态],[登记确认用户],[登记确认时间],[审核确认说明],[审核确认状态],[审核确认用户],[审核确认时间],[原始单据编号],[邮寄其它说明],[邮寄费用金额],[邮寄公司名称],[是否当场支付],[实际寄送日期],[邮寄确认状态],[邮寄确认用户]) " \
           r"VALUES (12,10456,1,3,'%s','中秋贺卡','2021-09-22','无','%s','一份','%s','%s','%s','200000','比较重要',null ,1,1359,'2021-09-23 10:37:51','同意',1,36,'2021-09-23 10:37:51',null ,'%s',0,'',0,null ,0,null )"

    sql2 = sql2 % (维护人, 客户姓名, 维护情况, 联系电话, 邮寄地址, 说明)
    print(sql2)
    cursor.execute(sql2,(维护人,客户姓名,维护情况,联系电话,邮寄地址,说明))
    conn.commit()

cursor.close()

# row = cursor.fetchone()
# while row:
#     print(row)
#     print("ID=%d, Name=%s" % (row[0], row[1]))
#     row = cursor.fetchone()

conn.close()

#
# cursor.execute("""
# IF OBJECT_ID('persons', 'U') IS NOT NULL
#     DROP TABLE persons
# CREATE TABLE persons (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     salesrep VARCHAR(100),
#     PRIMARY KEY(id)
# )
# """)
# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'),
#      (2, 'Jane Doe', 'Joe Dog'),
#      (3, 'Mike T.', 'Sarah H.')])
# # you must call commit() to persist your data if you don't set autocommit to True
# conn.commit()
