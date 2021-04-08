import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


df1= pd.read_csv('data.csv')
df2= pd.read_json('data.js')
df3= pd.read_csv('dirtydata.csv')

#df1.fillna(333.3, inplace=True)
#df3['Calories'].fillna(130, inplace=True)
#df3['Date']=pd.to_datetime(df3['Date'])
#df3.dropna(subset=['Date'], inplace=True)
#df3.loc[7, 'Duration']=45
#print(df1.tail(10))
#print(df3.to_string())

df1.plot()#x='Rank', y=['P25th','Median', 'P75th'])
plt.show()

#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()