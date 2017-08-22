#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding:utf-8 -*- 
import os,sys,shutil,re
from os.path import join, getsize
import numpy as np
import pandas as pd

# 模块针对的是.py文件，会将.py文件所有代码执行一遍，收集到所有的变量和函数待调用。
# 如果模块内包含类，则先需要在模块文件内实例化类。

class Init_vrc(object):
	"""docstring for Init_vrc"""
	def __init__(self):
		super(Init_vrc, self).__init__()
		self.list1 = [1,2,3,4,5,]
		self.mybsc_ip_d = {'黄石BSC10': '10.26.192.23', '黄石BSC11': '10.26.192.24', '黄石BSC12': '10.26.192.25', '黄石BSC13': '10.26.192.27', '黄石BSC14': '10.26.192.29', '黄石BSC15': '10.26.192.31', '黄石BSC16': '10.26.192.33', '黄石BSC17': '10.26.192.35', '黄石BSC02': '10.26.192.236', '黄石BSC04': '10.26.192.237', '黄石BSC05': '10.26.192.238', '黄石BSC07': '10.26.192.20', '黄石BSC08': '10.26.192.21', '黄石BSC09': '10.26.192.22'}



class CsvHandle(object):
	"""文件选取、跳过几行是属性，获取BSC列表是方法；属性的结果是静态的，方法的过程是动态的，结果是快照"""

	def __init__(self,mycsvfile,skiprows):
        super(CsvHandle, self).__init__()
		self.mycsv = mycsvfile
		self.skiprows = skiprows
		self.bscs = '网元名称'
		self.date = '起始时间'


	def get_bscs_date(self):
		df1 = pd.read_csv(self.mycsv,encoding='gbk',skiprows=self.skiprows)
		df1x = df1[self.bscs]
		df1x = df1x.drop_duplicates()
		bscs1 = list(df1x)
		
		df1y = df1[self.date]
		df1y = df1y.drop_duplicates()
		date = list(df1y)

		return bscs1,date


csv1handle = CsvHandle("./input/nb.csv",7) #实例化之后没有显性的输出或结果。实例化之后可以被调用，调用其中的属性和方法。

csv1handle.get_bscs_date()



def main():
	pass

if __name__ == '__main__':
	main()
	mydata = Init_vrc() # 初始化数据之后，在上一级命名空间，可以通过mydata.list1来访问属性