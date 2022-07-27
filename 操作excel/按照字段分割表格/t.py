import pandas as pd

df = pd.DataFrame(columns = ['name','age'])
print(df)

df.loc[0,'name'] = 'qq'
print(df)