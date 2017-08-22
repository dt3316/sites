#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding:utf-8 -*- 
#os.chdir('/Users/dongtao/Desktop/python3/项目hwmr/demo')

import os
import pandas as pd

file1 = 'bsc_ip.csv'

df1 = pd.read_csv(file1,encoding='gbk',skiprows=0)
print(df1.describe())


bsclist = df1["网元名称"]
bsclist = list(bsclist)

iplist = df1["ip"]
iplist = list(iplist)

result = dict(zip(bsclist,iplist))

print(result)


