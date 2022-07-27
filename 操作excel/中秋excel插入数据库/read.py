import pandas as pd
df = pd.read_excel('邮寄信息--2021中秋.xlsx')
df['维护人'] = df['维护人'].ffill()
df['联系电话'] = df['联系电话'].ffill()
df['维护情况'] = df['维护情况'].ffill()


for index,items in  df.iterrows():
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
    print(index,维护人,客户姓名,邮寄地址,联系电话,维护情况,五百,一千,两千,是否需要贺卡,备注,状态)
    # break




