"""
南北文件分拆
"""
import pandas as pd

path = 'G4水沟角铁分布表.csv'
df = pd.read_csv('G4水沟角铁分布表.csv', encoding='utf8')
r_h = df.iloc[:, 0]
l_h = df.iloc[:, 1]
r_b = df.iloc[:, 2]
l_b = df.iloc[:, 3]
r_w = df.iloc[:, 4]
l_w = df.iloc[:, 5]
r_t = df.iloc[:, 6]
l_t = df.iloc[:, 7]


class Name(object):

    def __init__(self, series, guizhe=1):
        self.guanhao = None
        self.south = None
        self.north = None
        self.series = series
        self.guizhe = guizhe
        self.clean_nan()

    def spilt(self):
        df = pd.DataFrame(self.series)

        df['guanhao'] = self.series[:].str.extract(r'(.*)/.*')
        self.guanhao = df['guanhao'][0]
        df['zhou'] = self.series[:].str.extract(r'/(\d+)[LR]{1}\d+[A-W]+$')
        df['zhou'] = df['zhou'][df['zhou'].isnull() == False].astype('float32')

        df['tiao'] = self.series[:].str.extract(r'/\d+[LR]{1}(\d+)[A-W]+$')
        df['tiao'] = df['tiao'][df['tiao'].isnull() == False].astype('float32')

        return df

    def clean_nan(self):
        self.series = self.series.drop(self.series[self.series.isnull()].index, axis=0)
        self.series = self.series.reset_index(drop=True)

    def differentiate(self):
        df = self.spilt()
        group = df.groupby('zhou')

        north, south = {}, {}

        for key, value in group:

            value = value.reset_index(drop=True)

            counter = None
            dividing = None
            last_index = value.iloc[:-1, :0].index.stop
            if self.guizhe <= 2:
                if self.guanhao == 'G2':
                    if key == 20:
                        dividing = 26
                    elif key == 6:
                        dividing = 34
                elif self.guanhao == 'G3':
                    if key == 20:
                        dividing = 19
                    elif key == 6:
                        dividing = 37
                elif self.guanhao == 'G4':
                    if key == 18:
                        dividing = 31
                    elif key == 6:
                        dividing = 41

            for i, val in value.iloc[:, -1].items():
                if counter:
                    counter += 1
                else:
                    counter = val
                if dividing:
                    if val == dividing:
                        north_ = value.iloc[:i, 0]
                        south_ = value.iloc[i:, :]
                        south_ = south_.sort_values(by=['tiao'], ascending=False)
                        south_ = south_.iloc[:, 0]
                        north_ = north_.reset_index(drop=True)
                        south_ = south_.reset_index(drop=True)
                        north[key] = north_
                        south[key] = south_

                        break

                if counter == val:
                    continue
                elif counter >= last_index*0.85:
                    # 顺序
                    if last_index < 3:
                        print(last_index)
                    index = last_index // 2
                    north_ = value.iloc[:index+1, 0]
                    south_ = value.iloc[index+1:, :]
                    south_ = south_.sort_values(by=['tiao'], ascending=False)
                    south_ = south_.iloc[:,0]
                    north_ = north_.reset_index(drop=True)
                    south_ = south_.reset_index(drop=True)
                    north[key] = north_
                    south[key] = south_
                elif counter != val:
                    north_ = value.iloc[:i, 0]
                    south_ = value.iloc[i:, :]
                    south_ = south_.sort_values(by=['tiao'], ascending=False)
                    south_ = south_.iloc[:, 0]
                    north_ = north_.reset_index(drop=True)
                    south_ = south_.reset_index(drop=True)
                    north[key] = north_
                    south[key] = south_

                    break

        return north, south

    def put_out(self):
        self.south = self.south.sort_values(by=['zhou', 'tiao'], ascending=False)
        self.north = self.north.sort_values(by=['zhou', 'tiao'], ascending=False)
        self.south = self.south.reset_index(drop=True)

        self.north = self.north.reset_index(drop=False)
        return self.south.iloc[:, 0], self.north.iloc[:, 0]


writer_s = pd.ExcelWriter('G4_S.xlsx')
writer_n = pd.ExcelWriter('G4_N.xlsx')
one = Name(r_h)
n1, s1 = one.differentiate()
#
two = Name(l_h)
n2, s2 = two.differentiate()

three = Name(r_b,3)
n3, s3 = three.differentiate()

four = Name(l_b,3)
n4, s4 = four.differentiate()

five = Name(r_w,3)
n5, s5 = five.differentiate()

six = Name(l_w,3)
n6, s6 = six.differentiate()

seven = Name(r_t,3)
n7, s7 = seven.differentiate()

eight = Name(l_t,3)
n8, s8 = eight.differentiate()
all_n = set(n1.keys()) | set(n2.keys()) | set(n3.keys()) | set(n4.keys()) | set(n5.keys()) | set(n6.keys()) | set(
    n7.keys()) | set(n8.keys())

sum_list_1 = []
for key in all_n:
    try:
        north1 = n1[key]
        sum_list_1.append(north1)
    except:
        north1 = pd.Series()
        # north1.name= 'R屋面角铁名称'
    try:
        north2 = n2[key]
        sum_list_1.append(north2)
    except:
        north2 = pd.Series()
        # north2.name='L屋面角铁名称'
    try:
        north3 = n3[key]
        sum_list_1.append(north3)
        print(north3)
    except:
        north3 = pd.Series()
        # north3.name='R百页角铁名称'
    try:
        north4 = n4[key]
        sum_list_1.append(north4)
    except:
        north4 = pd.Series()
    try:
        north5 = n5[key]
        sum_list_1.append(north5)
    except:
        north5 = pd.Series()

    try:
        north6 = n6[key]
        sum_list_1.append(north6)
    except:
        north6 = pd.Series()
    try:
        north7 = n7[key]
        sum_list_1.append(north7)
    except:
        north7 = pd.Series()
    try:
        north8 = n8[key]
        sum_list_1.append(north8)
    except:
        north8 = pd.Series()
    # north4.name='L百页角铁名称'

    North = pd.concat(sum_list_1, axis=1)
    sum_list_1=[]
    North.to_excel(writer_n, sheet_name=str(int(key)),index=False,startrow=1,index_label='kaixin')
    writer_n.save()

'------------'

all_s = set(s1.keys()) | set(s2.keys()) | set(s3.keys()) | set(s4.keys()) | set(s5.keys()) | set(s6.keys()) | set(
    s7.keys()) | set(s8.keys())
sum_list = []
for key in all_s:

    try:
        south1 = s1[key]
        sum_list.append(south1)
    except:
        south1 = pd.Series()
        # south1.name= 'R屋面角铁名称'
    try:
        south2 = s2[key]
        sum_list.append(south2)
    except:
        south2 = pd.Series()
        # south2.name='L屋面角铁名称'
    try:
        south3 = s3[key]
        sum_list.append(south3)
    except:
        south3 = pd.Series()
        # south3.name='R百页角铁名称'
    try:
        south4 = s4[key]
        sum_list.append(south4)
    except:
        south4 = pd.Series()
    try:
        south5 = s5[key]
        sum_list.append(south5)
    except:
        south5 = pd.Series()
    try:
        south6 = s6[key]
        sum_list.append(south6)
    except:
        south6 = pd.Series()
    try:
        south7 = s7[key]
        sum_list.append(south7)
    except:
        south7 = pd.Series()
    try:
        south8 = s8[key]
        sum_list.append(south8)
    except:
        south8 = pd.Series()
    # south4.name='L百页角铁名称'

    South = pd.concat(sum_list, axis=1)
    sum_list=[]
    South.to_excel(writer_s, sheet_name=str(int(key)),index=False,startrow=1)
    writer_n.save()

writer_s.close()
writer_n.close()
