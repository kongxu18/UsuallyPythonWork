import pandas

a = pandas.DataFrame(columns=['单体名称', '列号', '行号', '构件全称', '铝条编号', '下斜长度', '左角度', '右角度', '左切口长度', '右切口长度'])
print(a)

b = pandas.DataFrame(data=[(1, 2), (3, 4)])
b = b.reset_index(drop=True)
print(b)
