from cmath import inf
import csv

import pandas

df=[]
df1=[]
with open('dwarfstars_converted.csv','r') as f:
    r = csv.reader(f)
    for i in r:
        df.append(i)
headers1 = df[0]
dwarfstar_data = df[1:]

with open('brightestars.csv','r') as f:
    r = csv.reader(f)
    for i in r:
        df1.append(i)
headers2 = df1[0]
superstar_data = df1[1:]
data=[]

for i in superstar_data:
    data.append(i)
for i in dwarfstar_data:
    data.append(i)

with open('finalstars.csv','a+') as f:
    w = csv.writer(f)
    w.writerow(headers2)
    w.writerows(data)

d = pandas.read_csv('finalstars.csv')
d.drop(['Unnamed: 0','luminosity'],axis=1,inplace=True)
d.dropna()
d.reset_index(drop=True,inplace=True)
d.to_csv('cleanedstarsdata.csv')
print(d.tail(8))
print(d.dtypes)