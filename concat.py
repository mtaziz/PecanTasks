import pandas as pd
df1=pd.read_csv('2002.csv')
df2=pd.read_csv('2003.csv')
df3=pd.read_csv('2004.csv')
df4=pd.read_csv('2005.csv')
df = pd.concat([df1,df2,df3,df4])
df.to_csv('LAI.csv',index=True, header=True)