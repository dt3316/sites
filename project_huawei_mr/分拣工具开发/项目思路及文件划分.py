输入部分：

=====================================================
变量：
BSC名称来自MR文件
文件名中IP来自字符串截取
pandas.to_csv 来自于最终目录JOIN MMLTXT文件

使用函数的时候，return出多个变量的元组，通过元组index访问成list，变量可以被函数体外其他函数处理


=====================================================


=====================================================
1、先读取mml文件夹下的所有txt文件：方法：函数+return
=====================================================






=====================================================
2、对文件名进行字符串截取，截取出IP地址
=====================================================






=====================================================
3、核对IP地址与BSC之间的映射关系
=====================================================




=====================================================
4、文件夹相关操作:ms\20150628\黄石BSC02\mmltxt
=====================================================

shutil.copyfile( src, dst)


=====================================================
4.1、时间与字符串处理：
	从字符串到时间一一对应才行
	'04/23/2017 08:00:00' 
			对应"%m/%d/%Y %H:%M:%S"
	'04/23/2017' 
			对应"%m/%d/%Y"
	从时间到字符串，用
	'%Y%m%d' 对应#20170628
	'%Y%Y%m%d' 对应#20170170628

=====================================================


=====================================================
单元1 通过处理3个文件，得出3个不同的日期BSC，对比，一致，取其中一个，输出唯一日期，唯一BSC
=====================================================



import os,sys,shutil
import pandas as pd
from datetime import datetime
from itertools import chain

csv_file_full = "full.csv"
csv_file_nb = "nb.csv"
csv_file_half = "half.csv"


def daynbsc_full(csv_file_full):
	csv_file = "full.csv"
	skip_row = 8
	df_full = pd.read_csv(csv_file,encoding='gbk',skiprows=skip_row-1)
	df_fullbsc = df_full['网元名称']
	df_fullbsc = df_fullbsc.drop_duplicates()
	bscs_full=list(df_fullbsc)
	df_fulldays = df_full['起始时间']
	df_fulldays = df_fulldays.drop_duplicates()
	days_full = list(df_fulldays)
	
	return days_full,bscs_full,df_full ##输出的是元组([days],[bscs],df)

def daynbsc_half(csv_file_half):
	csv_file = "half.csv"
	skip_row = 8
	df_half = pd.read_csv(csv_file,encoding='gbk',skiprows=skip_row-1)
	df_halfbsc = df_half['网元名称']
	df_halfbsc = df_halfbsc.drop_duplicates()
	bscs_half=list(df_halfbsc)
	df_halfdays = df_half['起始时间']
	df_halfdays = df_halfdays.drop_duplicates()
	days_half = list(df_halfdays)
	
	return days_half,bscs_half,df_half #输出的是元组([days],[bscs],df)

def daynbsc_nb(csv_file_nb):
	csv_file = "nb.csv"
	skip_row = 8
	df_nb = pd.read_csv(csv_file,encoding='gbk',skiprows=skip_row-1)
	df_nbbsc = df_nb['网元名称']
	df_nbbsc = df_nbbsc.drop_duplicates()
	bscs_nb=list(df_nbbsc)
	df_nbdays = df_nb['起始时间']
	df_nbdays = df_nbdays.drop_duplicates()
	days_nb = list(df_nbdays)
	
	return days_nb,bscs_nb,df_nb #输出的是元组([days],[bscs],df)

def day8digi(listday): #csv起始时间列年月日时分秒输出成为8位数字符
	# ptime要把字符串对应到年月日时分秒，而ftime格式化成字符串dtstr是字符串dtdt是真的时间
	daylist = []
	for index in range(len(listday)):
		dtdt = datetime.strptime(listday[index], "%m/%d/%Y %H:%M:%S")
		day8 = dtdt.strftime('%Y%m%d') #20170628
		daylist.append(day8)
	days=list(set(daylist))
	return days

def collect():

	daynbsc_half = daynbsc_half(csv_file_half)
	daynbsc_full = daynbsc_full(csv_file_full)
	daynbsc_nb = daynbsc_nb(csv_file_nb)

	days_half = daynbsc_half[0]
	days_full = daynbsc_full[0]
	days_nb = daynbsc_nb[0]

	bscs_half = daynbsc_half[1]
	bscs_full = daynbsc_full[1]
	bscs_nb = daynbsc_nb[1]

	df_half = daynbsc_half[2]
	df_full = daynbsc_full[2]
	df_nb = daynbsc_nb[2]

	days_uniq = day8digi(listday)
	bscs_uniq = list(set(chain.from_iterable(zip(bscs_nb, bscs_half,bscs_full))))

collect() #执行

#给3个文件，可以输出唯一的日期和唯一的BSC



=====================================================
单元2 使用两次循环创建文件夹\ms\20150628\黄石BSC02\mmltxt
=====================================================


def make_folders(days_uniq,bscs_uniq,df_half,df_full,df_nb):
	msfolder = './ms/'
	if os.path.exists(msfolder):
		shutil.rmtree(msfolder)
	else:
		pass
	os.mkdir(msfolder)
	currdir = os.path.join(os.path.abspath('.'),'ms')

	h04columns = ['起始时间','周期','网元名称','Cell','TRX','S4100C:半速率TCH上行接收电平等级0接收质量等级0的次数 (无)','S4100D:半速率TCH下行接收电平等级0接收质量等级0的次数 (无)','S4101C:半速率TCH上行接收电平等级0接收质量等级1的次数 (无)','S4101D:半速率TCH下行接收电平等级0接收质量等级1的次数 (无)','S4102C:半速率TCH上行接收电平等级0接收质量等级2的次数 (无)','S4102D:半速率TCH下行接收电平等级0接收质量等级2的次数 (无)','S4103C:半速率TCH上行接收电平等级0接收质量等级3的次数 (无)','S4103D:半速率TCH下行接收电平等级0接收质量等级3的次数 (无)','S4104C:半速率TCH上行接收电平等级0接收质量等级4的次数 (无)','S4104D:半速率TCH下行接收电平等级0接收质量等级4的次数 (无)','S4105C:半速率TCH上行接收电平等级0接收质量等级5的次数 (无)','S4105D:半速率TCH下行接收电平等级0接收质量等级5的次数 (无)','S4106C:半速率TCH上行接收电平等级0接收质量等级6的次数 (无)','S4106D:半速率TCH下行接收电平等级0接收质量等级6的次数 (无)','S4107C:半速率TCH上行接收电平等级0接收质量等级7的次数 (无)','S4107D:半速率TCH下行接收电平等级0接收质量等级7的次数 (无)','S4110C:半速率TCH上行接收电平等级1接收质量等级0的次数 (无)','S4110D:半速率TCH下行接收电平等级1接收质量等级0的次数 (无)','S4111C:半速率TCH上行接收电平等级1接收质量等级1的次数 (无)','S4111D:半速率TCH下行接收电平等级1接收质量等级1的次数 (无)','S4112C:半速率TCH上行接收电平等级1接收质量等级2的次数 (无)','S4112D:半速率TCH下行接收电平等级1接收质量等级2的次数 (无)','S4113C:半速率TCH上行接收电平等级1接收质量等级3的次数 (无)','S4113D:半速率TCH下行接收电平等级1接收质量等级3的次数 (无)','S4114C:半速率TCH上行接收电平等级1接收质量等级4的次数 (无)','S4114D:半速率TCH下行接收电平等级1接收质量等级4的次数 (无)','S4115C:半速率TCH上行接收电平等级1接收质量等级5的次数 (无)','S4115D:半速率TCH下行接收电平等级1接收质量等级5的次数 (无)','S4116C:半速率TCH上行接收电平等级1接收质量等级6的次数 (无)','S4116D:半速率TCH下行接收电平等级1接收质量等级6的次数 (无)','S4117C:半速率TCH上行接收电平等级1接收质量等级7的次数 (无)','S4117D:半速率TCH下行接收电平等级1接收质量等级7的次数 (无)','S4120C:半速率TCH上行接收电平等级2接收质量等级0的次数 (无)','S4120D:半速率TCH下行接收电平等级2接收质量等级0的次数 (无)','S4121C:半速率TCH上行接收电平等级2接收质量等级1的次数 (无)','S4121D:半速率TCH下行接收电平等级2接收质量等级1的次数 (无)','S4122C:半速率TCH上行接收电平等级2接收质量等级2的次数 (无)','S4122D:半速率TCH下行接收电平等级2接收质量等级2的次数 (无)','S4123C:半速率TCH上行接收电平等级2接收质量等级3的次数 (无)','S4123D:半速率TCH下行接收电平等级2接收质量等级3的次数 (无)','S4124C:半速率TCH上行接收电平等级2接收质量等级4的次数 (无)','S4124D:半速率TCH下行接收电平等级2接收质量等级4的次数 (无)','S4125C:半速率TCH上行接收电平等级2接收质量等级5的次数 (无)','S4125D:半速率TCH下行接收电平等级2接收质量等级5的次数 (无)','S4126C:半速率TCH上行接收电平等级2接收质量等级6的次数 (无)','S4126D:半速率TCH下行接收电平等级2接收质量等级6的次数 (无)','S4127C:半速率TCH上行接收电平等级2接收质量等级7的次数 (无)','S4127D:半速率TCH下行接收电平等级2接收质量等级7的次数 (无)','S4130C:半速率TCH上行接收电平等级3接收质量等级0的次数 (无)','S4130D:半速率TCH下行接收电平等级3接收质量等级0的次数 (无)','S4131C:半速率TCH上行接收电平等级3接收质量等级1的次数 (无)','S4131D:半速率TCH下行接收电平等级3接收质量等级1的次数 (无)','S4132C:半速率TCH上行接收电平等级3接收质量等级2的次数 (无)','S4132D:半速率TCH下行接收电平等级3接收质量等级2的次数 (无)','S4133C:半速率TCH上行接收电平等级3接收质量等级3的次数 (无)','S4133D:半速率TCH下行接收电平等级3接收质量等级3的次数 (无)','S4134C:半速率TCH上行接收电平等级3接收质量等级4的次数 (无)','S4134D:半速率TCH下行接收电平等级3接收质量等级4的次数 (无)','S4135C:半速率TCH上行接收电平等级3接收质量等级5的次数 (无)','S4135D:半速率TCH下行接收电平等级3接收质量等级5的次数 (无)','S4136C:半速率TCH上行接收电平等级3接收质量等级6的次数 (无)','S4136D:半速率TCH下行接收电平等级3接收质量等级6的次数 (无)','S4137C:半速率TCH上行接收电平等级3接收质量等级7的次数 (无)','S4137D:半速率TCH下行接收电平等级3接收质量等级7的次数 (无)','S4140C:半速率TCH上行接收电平等级4接收质量等级0的次数 (无)','S4140D:半速率TCH下行接收电平等级4接收质量等级0的次数 (无)','S4141C:半速率TCH上行接收电平等级4接收质量等级1的次数 (无)','S4141D:半速率TCH下行接收电平等级4接收质量等级1的次数 (无)','S4142C:半速率TCH上行接收电平等级4接收质量等级2的次数 (无)','S4142D:半速率TCH下行接收电平等级4接收质量等级2的次数 (无)','S4143C:半速率TCH上行接收电平等级4接收质量等级3的次数 (无)','S4143D:半速率TCH下行接收电平等级4接收质量等级3的次数 (无)','S4144C:半速率TCH上行接收电平等级4接收质量等级4的次数 (无)','S4144D:半速率TCH下行接收电平等级4接收质量等级4的次数 (无)','S4145C:半速率TCH上行接收电平等级4接收质量等级5的次数 (无)','S4145D:半速率TCH下行接收电平等级4接收质量等级5的次数 (无)','S4146C:半速率TCH上行接收电平等级4接收质量等级6的次数 (无)','S4146D:半速率TCH下行接收电平等级4接收质量等级6的次数 (无)','S4147C:半速率TCH上行接收电平等级4接收质量等级7的次数 (无)','S4147D:半速率TCH下行接收电平等级4接收质量等级7的次数 (无)']
	h57columns = ['起始时间','周期','网元名称','Cell','TRX','S4150C:半速率TCH上行接收电平等级5接收质量等级0的次数 (无)','S4150D:半速率TCH下行接收电平等级5接收质量等级0的次数 (无)','S4151C:半速率TCH上行接收电平等级5接收质量等级1的次数 (无)','S4151D:半速率TCH下行接收电平等级5接收质量等级1的次数 (无)','S4152C:半速率TCH上行接收电平等级5接收质量等级2的次数 (无)','S4152D:半速率TCH下行接收电平等级5接收质量等级2的次数 (无)','S4153C:半速率TCH上行接收电平等级5接收质量等级3的次数 (无)','S4153D:半速率TCH下行接收电平等级5接收质量等级3的次数 (无)','S4154C:半速率TCH上行接收电平等级5接收质量等级4的次数 (无)','S4154D:半速率TCH下行接收电平等级5接收质量等级4的次数 (无)','S4155C:半速率TCH上行接收电平等级5接收质量等级5的次数 (无)','S4155D:半速率TCH下行接收电平等级5接收质量等级5的次数 (无)','S4156C:半速率TCH上行接收电平等级5接收质量等级6的次数 (无)','S4156D:半速率TCH下行接收电平等级5接收质量等级6的次数 (无)','S4157C:半速率TCH上行接收电平等级5接收质量等级7的次数 (无)','S4157D:半速率TCH下行接收电平等级5接收质量等级7的次数 (无)','S4160C:半速率TCH上行接收电平等级6接收质量等级0的次数 (无)','S4160D:半速率TCH下行接收电平等级6接收质量等级0的次数 (无)','S4161C:半速率TCH上行接收电平等级6接收质量等级1的次数 (无)','S4161D:半速率TCH下行接收电平等级6接收质量等级1的次数 (无)','S4162C:半速率TCH上行接收电平等级6接收质量等级2的次数 (无)','S4162D:半速率TCH下行接收电平等级6接收质量等级2的次数 (无)','S4163C:半速率TCH上行接收电平等级6接收质量等级3的次数 (无)','S4163D:半速率TCH下行接收电平等级6接收质量等级3的次数 (无)','S4164C:半速率TCH上行接收电平等级6接收质量等级4的次数 (无)','S4164D:半速率TCH下行接收电平等级6接收质量等级4的次数 (无)','S4165C:半速率TCH上行接收电平等级6接收质量等级5的次数 (无)','S4165D:半速率TCH下行接收电平等级6接收质量等级5的次数 (无)','S4166C:半速率TCH上行接收电平等级6接收质量等级6的次数 (无)','S4166D:半速率TCH下行接收电平等级6接收质量等级6的次数 (无)','S4167C:半速率TCH上行接收电平等级6接收质量等级7的次数 (无)','S4167D:半速率TCH下行接收电平等级6接收质量等级7的次数 (无)','S4170C:半速率TCH上行接收电平等级7接收质量等级0的次数 (无)','S4170D:半速率TCH下行接收电平等级7接收质量等级0的次数 (无)','S4171C:半速率TCH上行接收电平等级7接收质量等级1的次数 (无)','S4171D:半速率TCH下行接收电平等级7接收质量等级1的次数 (无)','S4172C:半速率TCH上行接收电平等级7接收质量等级2的次数 (无)','S4172D:半速率TCH下行接收电平等级7接收质量等级2的次数 (无)','S4173C:半速率TCH上行接收电平等级7接收质量等级3的次数 (无)','S4173D:半速率TCH下行接收电平等级7接收质量等级3的次数 (无)','S4174C:半速率TCH上行接收电平等级7接收质量等级4的次数 (无)','S4174D:半速率TCH下行接收电平等级7接收质量等级4的次数 (无)','S4175C:半速率TCH上行接收电平等级7接收质量等级5的次数 (无)','S4175D:半速率TCH下行接收电平等级7接收质量等级5的次数 (无)','S4176C:半速率TCH上行接收电平等级7接收质量等级6的次数 (无)','S4176D:半速率TCH下行接收电平等级7接收质量等级6的次数 (无)','S4177C:半速率TCH上行接收电平等级7接收质量等级7的次数 (无)','S4177D:半速率TCH下行接收电平等级7接收质量等级7的次数 (无)']
	f04columns = ['起始时间','周期','网元名称','Cell','TRX','S4100A:全速率TCH上行接收电平等级0接收质量等级0的次数 (无)','S4100B:全速率TCH下行接收电平等级0接收质量等级0的次数 (无)','S4101A:全速率TCH上行接收电平等级0接收质量等级1的次数 (无)','S4101B:全速率TCH下行接收电平等级0接收质量等级1的次数 (无)','S4102A:全速率TCH上行接收电平等级0接收质量等级2的次数 (无)','S4102B:全速率TCH下行接收电平等级0接收质量等级2的次数 (无)','S4103A:全速率TCH上行接收电平等级0接收质量等级3的次数 (无)','S4103B:全速率TCH下行接收电平等级0接收质量等级3的次数 (无)','S4104A:全速率TCH上行接收电平等级0接收质量等级4的次数 (无)','S4104B:全速率TCH下行接收电平等级0接收质量等级4的次数 (无)','S4105A:全速率TCH上行接收电平等级0接收质量等级5的次数 (无)','S4105B:全速率TCH下行接收电平等级0接收质量等级5的次数 (无)','S4106A:全速率TCH上行接收电平等级0接收质量等级6的次数 (无)','S4106B:全速率TCH下行接收电平等级0接收质量等级6的次数 (无)','S4107A:全速率TCH上行接收电平等级0接收质量等级7的次数 (无)','S4107B:全速率TCH下行接收电平等级0接收质量等级7的次数 (无)','S4110A:全速率TCH上行接收电平等级1接收质量等级0的次数 (无)','S4110B:全速率TCH下行接收电平等级1接收质量等级0的次数 (无)','S4111A:全速率TCH上行接收电平等级1接收质量等级1的次数 (无)','S4111B:全速率TCH下行接收电平等级1接收质量等级1的次数 (无)','S4112A:全速率TCH上行接收电平等级1接收质量等级2的次数 (无)','S4112B:全速率TCH下行接收电平等级1接收质量等级2的次数 (无)','S4113A:全速率TCH上行接收电平等级1接收质量等级3的次数 (无)','S4113B:全速率TCH下行接收电平等级1接收质量等级3的次数 (无)','S4114A:全速率TCH上行接收电平等级1接收质量等级4的次数 (无)','S4114B:全速率TCH下行接收电平等级1接收质量等级4的次数 (无)','S4115A:全速率TCH上行接收电平等级1接收质量等级5的次数 (无)','S4115B:全速率TCH下行接收电平等级1接收质量等级5的次数 (无)','S4116A:全速率TCH上行接收电平等级1接收质量等级6的次数 (无)','S4116B:全速率TCH下行接收电平等级1接收质量等级6的次数 (无)','S4117A:全速率TCH上行接收电平等级1接收质量等级7的次数 (无)','S4117B:全速率TCH下行接收电平等级1接收质量等级7的次数 (无)','S4120A:全速率TCH上行接收电平等级2接收质量等级0的次数 (无)','S4120B:全速率TCH下行接收电平等级2接收质量等级0的次数 (无)','S4121A:全速率TCH上行接收电平等级2接收质量等级1的次数 (无)','S4121B:全速率TCH下行接收电平等级2接收质量等级1的次数 (无)','S4122A:全速率TCH上行接收电平等级2接收质量等级2的次数 (无)','S4122B:全速率TCH下行接收电平等级2接收质量等级2的次数 (无)','S4123A:全速率TCH上行接收电平等级2接收质量等级3的次数 (无)','S4123B:全速率TCH下行接收电平等级2接收质量等级3的次数 (无)','S4124A:全速率TCH上行接收电平等级2接收质量等级4的次数 (无)','S4124B:全速率TCH下行接收电平等级2接收质量等级4的次数 (无)','S4125A:全速率TCH上行接收电平等级2接收质量等级5的次数 (无)','S4125B:全速率TCH下行接收电平等级2接收质量等级5的次数 (无)','S4126A:全速率TCH上行接收电平等级2接收质量等级6的次数 (无)','S4126B:全速率TCH下行接收电平等级2接收质量等级6的次数 (无)','S4127A:全速率TCH上行接收电平等级2接收质量等级7的次数 (无)','S4127B:全速率TCH下行接收电平等级2接收质量等级7的次数 (无)','S4130A:全速率TCH上行接收电平等级3接收质量等级0的次数 (无)','S4130B:全速率TCH下行接收电平等级3接收质量等级0的次数 (无)','S4131A:全速率TCH上行接收电平等级3接收质量等级1的次数 (无)','S4131B:全速率TCH下行接收电平等级3接收质量等级1的次数 (无)','S4132A:全速率TCH上行接收电平等级3接收质量等级2的次数 (无)','S4132B:全速率TCH下行接收电平等级3接收质量等级2的次数 (无)','S4133A:全速率TCH上行接收电平等级3接收质量等级3的次数 (无)','S4133B:全速率TCH下行接收电平等级3接收质量等级3的次数 (无)','S4134A:全速率TCH上行接收电平等级3接收质量等级4的次数 (无)','S4134B:全速率TCH下行接收电平等级3接收质量等级4的次数 (无)','S4135A:全速率TCH上行接收电平等级3接收质量等级5的次数 (无)','S4135B:全速率TCH下行接收电平等级3接收质量等级5的次数 (无)','S4136A:全速率TCH上行接收电平等级3接收质量等级6的次数 (无)','S4136B:全速率TCH下行接收电平等级3接收质量等级6的次数 (无)','S4137A:全速率TCH上行接收电平等级3接收质量等级7的次数 (无)','S4137B:全速率TCH下行接收电平等级3接收质量等级7的次数 (无)','S4140A:全速率TCH上行接收电平等级4接收质量等级0的次数 (无)','S4140B:全速率TCH下行接收电平等级4接收质量等级0的次数 (无)','S4141A:全速率TCH上行接收电平等级4接收质量等级1的次数 (无)','S4141B:全速率TCH下行接收电平等级4接收质量等级1的次数 (无)','S4142A:全速率TCH上行接收电平等级4接收质量等级2的次数 (无)','S4142B:全速率TCH下行接收电平等级4接收质量等级2的次数 (无)','S4143A:全速率TCH上行接收电平等级4接收质量等级3的次数 (无)','S4143B:全速率TCH下行接收电平等级4接收质量等级3的次数 (无)','S4144A:全速率TCH上行接收电平等级4接收质量等级4的次数 (无)','S4144B:全速率TCH下行接收电平等级4接收质量等级4的次数 (无)','S4145A:全速率TCH上行接收电平等级4接收质量等级5的次数 (无)','S4145B:全速率TCH下行接收电平等级4接收质量等级5的次数 (无)','S4146A:全速率TCH上行接收电平等级4接收质量等级6的次数 (无)','S4146B:全速率TCH下行接收电平等级4接收质量等级6的次数 (无)','S4147A:全速率TCH上行接收电平等级4接收质量等级7的次数 (无)','S4147B:全速率TCH下行接收电平等级4接收质量等级7的次数 (无)']
	f57columns = ['起始时间','周期','网元名称','Cell','TRX','S4150A:全速率TCH上行接收电平等级5接收质量等级0的次数 (无)','S4150B:全速率TCH下行接收电平等级5接收质量等级0的次数 (无)','S4151A:全速率TCH上行接收电平等级5接收质量等级1的次数 (无)','S4151B:全速率TCH下行接收电平等级5接收质量等级1的次数 (无)','S4152A:全速率TCH上行接收电平等级5接收质量等级2的次数 (无)','S4152B:全速率TCH下行接收电平等级5接收质量等级2的次数 (无)','S4153A:全速率TCH上行接收电平等级5接收质量等级3的次数 (无)','S4153B:全速率TCH下行接收电平等级5接收质量等级3的次数 (无)','S4154A:全速率TCH上行接收电平等级5接收质量等级4的次数 (无)','S4154B:全速率TCH下行接收电平等级5接收质量等级4的次数 (无)','S4155A:全速率TCH上行接收电平等级5接收质量等级5的次数 (无)','S4155B:全速率TCH下行接收电平等级5接收质量等级5的次数 (无)','S4156A:全速率TCH上行接收电平等级5接收质量等级6的次数 (无)','S4156B:全速率TCH下行接收电平等级5接收质量等级6的次数 (无)','S4157A:全速率TCH上行接收电平等级5接收质量等级7的次数 (无)','S4157B:全速率TCH下行接收电平等级5接收质量等级7的次数 (无)','S4160A:全速率TCH上行接收电平等级6接收质量等级0的次数 (无)','S4160B:全速率TCH下行接收电平等级6接收质量等级0的次数 (无)','S4161A:全速率TCH上行接收电平等级6接收质量等级1的次数 (无)','S4161B:全速率TCH下行接收电平等级6接收质量等级1的次数 (无)','S4162A:全速率TCH上行接收电平等级6接收质量等级2的次数 (无)','S4162B:全速率TCH下行接收电平等级6接收质量等级2的次数 (无)','S4163A:全速率TCH上行接收电平等级6接收质量等级3的次数 (无)','S4163B:全速率TCH下行接收电平等级6接收质量等级3的次数 (无)','S4164A:全速率TCH上行接收电平等级6接收质量等级4的次数 (无)','S4164B:全速率TCH下行接收电平等级6接收质量等级4的次数 (无)','S4165A:全速率TCH上行接收电平等级6接收质量等级5的次数 (无)','S4165B:全速率TCH下行接收电平等级6接收质量等级5的次数 (无)','S4166A:全速率TCH上行接收电平等级6接收质量等级6的次数 (无)','S4166B:全速率TCH下行接收电平等级6接收质量等级6的次数 (无)','S4167A:全速率TCH上行接收电平等级6接收质量等级7的次数 (无)','S4167B:全速率TCH下行接收电平等级6接收质量等级7的次数 (无)','S4170A:全速率TCH上行接收电平等级7接收质量等级0的次数 (无)','S4170B:全速率TCH下行接收电平等级7接收质量等级0的次数 (无)','S4171A:全速率TCH上行接收电平等级7接收质量等级1的次数 (无)','S4171B:全速率TCH下行接收电平等级7接收质量等级1的次数 (无)','S4172A:全速率TCH上行接收电平等级7接收质量等级2的次数 (无)','S4172B:全速率TCH下行接收电平等级7接收质量等级2的次数 (无)','S4173A:全速率TCH上行接收电平等级7接收质量等级3的次数 (无)','S4173B:全速率TCH下行接收电平等级7接收质量等级3的次数 (无)','S4174A:全速率TCH上行接收电平等级7接收质量等级4的次数 (无)','S4174B:全速率TCH下行接收电平等级7接收质量等级4的次数 (无)','S4175A:全速率TCH上行接收电平等级7接收质量等级5的次数 (无)','S4175B:全速率TCH下行接收电平等级7接收质量等级5的次数 (无)','S4176A:全速率TCH上行接收电平等级7接收质量等级6的次数 (无)','S4176B:全速率TCH下行接收电平等级7接收质量等级6的次数 (无)','S4177A:全速率TCH上行接收电平等级7接收质量等级7的次数 (无)','S4177B:全速率TCH下行接收电平等级7接收质量等级7的次数 (无)']
	nbcolumns = ["起始时间","周期","网元名称","GCELL_NCELL","BCCH","BCC,NCC","NCC","AS360:邻近小区平均信号强度 (分贝)","AS362:服务小区与邻区信号强度差平均值 (分贝)","S360:邻近小区信号强度 (分贝)","S361:邻近小区测量报告数目 (无)","S362:服务小区信号强度 (分贝)","S363:服务小区与邻区信号强度差小于邻区干扰电平门限1的测量报告数 (无)","S364:服务小区与邻区信号强度差大于邻区干扰电平门限1的测量报告数 (无)","S365:服务小区与邻区信号强度差大于邻区干扰电平门限2的测量报告数 (无)","S366:服务小区与邻区信号强度差大于邻区干扰电平门限3的测量报告数 (无)","S367:服务小区与邻区信号强度差大于邻区干扰电平门限4的测量报告数 (无)","S368:服务小区与邻区信号强度差大于邻区干扰电平门限5的测量报告数 (无)","S369:服务小区与邻区信号强度差大于邻区干扰电平门限6的测量报告数 (无)","S370:服务小区与邻区信号强度差大于邻区干扰电平门限7的测量报告数 (无)","S371:邻区与服务小区信号强度差大于相对电平门限的测量报告数 (无)","S372:邻区信号强度大于绝对电平门限的测量报告数 (无)","S386:竞争小区信号处于电平等级0的次数 (无)","S387:竞争小区信号处于电平等级1的次数 (无)","S388:竞争小区信号处于电平等级2的次数 (无)","S389:竞争小区信号处于电平等级3的次数 (无)","S390:竞争小区信号处于电平等级4的次数 (无)","S391:竞争小区信号处于电平等级5的次数 (无)","S392:竞争小区信号处于电平等级6的次数 (无)","S393:竞争小区信号处于电平等级7的次数 (无)","S394:服务小区与邻区信号强度差小于邻区干扰电平门限0的测量报告数 (无)"]

	for index in range(len(days_uniq)): #外层循环按日期循环
			joineddir = os.path.join(currdir,days_uniq[index])
			print('准备建目录',joineddir)
			os.mkdir(joineddir)
			for index in range(len(bscs_uniq)): #内层循环，按BSC循环
				joineddir1 = os.path.join(joineddir,bscs_uniq[index])
				os.mkdir(joineddir1)
				print('目录',joineddir1)

				joined_full04 = os.path.join(joineddir1,'全速率0-4.csv')
				joined_full57 = os.path.join(joineddir1,'全速率5-7.csv')
				joined_half04 = os.path.join(joineddir1,'半速率0-4.csv')
				joined_half57 = os.path.join(joineddir1,'半速率5-7.csv')
				joined_nb = os.path.join(joineddir1,'邻区测量.csv')
				
				df_full = df1[df_full['网元名称']==days_uniq[index]] #按照BSC筛选
				df_half= df1[df_half['网元名称']==days_uniq[index]] #按照BSC筛选
				df_nb = df1[df_nb['网元名称']==days_uniq[index]] #按照BSC筛选

				df_full.to_csv(joined_full04,encoding='gbk',columns=f04columns,index=False,header=True)
				print('文件',joined_full04)
				df_full.to_csv(joined_full57,encoding='gbk',columns=f57columns,index=False,header=True)
				print('文件',joined_full57)
				df_half.to_csv(joined_half04,encoding='gbk',columns=h04columns,index=False,header=True)
				print('文件',joined_half04)
				df_half.to_csv(joined_half57,encoding='gbk',columns=h57columns,index=False,header=True)
				print('文件',joined_half57)
				df_nb.to_csv(joined_nb,encoding='gbk',columns=nbcolumns,index=False,header=True)
				print('文件',joined_nb)

				
				
				
				

make_folders = make_folders(days_uniq,bscs_uniq,df_half,df_full,df_nb)




=====================================================
单元4 处理文件，读取csv的时候，return过一个df，需要处理成to_csv







=====================================================



单测代码：=====文件循环~~~

files = ['half.csv','full.csv','hr.csv','mml-192.168.1.2-2017.txt']

for index in range(len(files)):
	curfile = files[index]
	print('file:',curfile)

单测代码：=====文件循环end


单测代码：===== 单文件分拣~~~

import pandas as pd

h04columns = ['起始时间','周期','网元名称','Cell','TRX','S4100C:半速率TCH上行接收电平等级0接收质量等级0的次数 (无)','S4100D:半速率TCH下行接收电平等级0接收质量等级0的次数 (无)','S4101C:半速率TCH上行接收电平等级0接收质量等级1的次数 (无)','S4101D:半速率TCH下行接收电平等级0接收质量等级1的次数 (无)','S4102C:半速率TCH上行接收电平等级0接收质量等级2的次数 (无)','S4102D:半速率TCH下行接收电平等级0接收质量等级2的次数 (无)','S4103C:半速率TCH上行接收电平等级0接收质量等级3的次数 (无)','S4103D:半速率TCH下行接收电平等级0接收质量等级3的次数 (无)','S4104C:半速率TCH上行接收电平等级0接收质量等级4的次数 (无)','S4104D:半速率TCH下行接收电平等级0接收质量等级4的次数 (无)','S4105C:半速率TCH上行接收电平等级0接收质量等级5的次数 (无)','S4105D:半速率TCH下行接收电平等级0接收质量等级5的次数 (无)','S4106C:半速率TCH上行接收电平等级0接收质量等级6的次数 (无)','S4106D:半速率TCH下行接收电平等级0接收质量等级6的次数 (无)','S4107C:半速率TCH上行接收电平等级0接收质量等级7的次数 (无)','S4107D:半速率TCH下行接收电平等级0接收质量等级7的次数 (无)','S4110C:半速率TCH上行接收电平等级1接收质量等级0的次数 (无)','S4110D:半速率TCH下行接收电平等级1接收质量等级0的次数 (无)','S4111C:半速率TCH上行接收电平等级1接收质量等级1的次数 (无)','S4111D:半速率TCH下行接收电平等级1接收质量等级1的次数 (无)','S4112C:半速率TCH上行接收电平等级1接收质量等级2的次数 (无)','S4112D:半速率TCH下行接收电平等级1接收质量等级2的次数 (无)','S4113C:半速率TCH上行接收电平等级1接收质量等级3的次数 (无)','S4113D:半速率TCH下行接收电平等级1接收质量等级3的次数 (无)','S4114C:半速率TCH上行接收电平等级1接收质量等级4的次数 (无)','S4114D:半速率TCH下行接收电平等级1接收质量等级4的次数 (无)','S4115C:半速率TCH上行接收电平等级1接收质量等级5的次数 (无)','S4115D:半速率TCH下行接收电平等级1接收质量等级5的次数 (无)','S4116C:半速率TCH上行接收电平等级1接收质量等级6的次数 (无)','S4116D:半速率TCH下行接收电平等级1接收质量等级6的次数 (无)','S4117C:半速率TCH上行接收电平等级1接收质量等级7的次数 (无)','S4117D:半速率TCH下行接收电平等级1接收质量等级7的次数 (无)','S4120C:半速率TCH上行接收电平等级2接收质量等级0的次数 (无)','S4120D:半速率TCH下行接收电平等级2接收质量等级0的次数 (无)','S4121C:半速率TCH上行接收电平等级2接收质量等级1的次数 (无)','S4121D:半速率TCH下行接收电平等级2接收质量等级1的次数 (无)','S4122C:半速率TCH上行接收电平等级2接收质量等级2的次数 (无)','S4122D:半速率TCH下行接收电平等级2接收质量等级2的次数 (无)','S4123C:半速率TCH上行接收电平等级2接收质量等级3的次数 (无)','S4123D:半速率TCH下行接收电平等级2接收质量等级3的次数 (无)','S4124C:半速率TCH上行接收电平等级2接收质量等级4的次数 (无)','S4124D:半速率TCH下行接收电平等级2接收质量等级4的次数 (无)','S4125C:半速率TCH上行接收电平等级2接收质量等级5的次数 (无)','S4125D:半速率TCH下行接收电平等级2接收质量等级5的次数 (无)','S4126C:半速率TCH上行接收电平等级2接收质量等级6的次数 (无)','S4126D:半速率TCH下行接收电平等级2接收质量等级6的次数 (无)','S4127C:半速率TCH上行接收电平等级2接收质量等级7的次数 (无)','S4127D:半速率TCH下行接收电平等级2接收质量等级7的次数 (无)','S4130C:半速率TCH上行接收电平等级3接收质量等级0的次数 (无)','S4130D:半速率TCH下行接收电平等级3接收质量等级0的次数 (无)','S4131C:半速率TCH上行接收电平等级3接收质量等级1的次数 (无)','S4131D:半速率TCH下行接收电平等级3接收质量等级1的次数 (无)','S4132C:半速率TCH上行接收电平等级3接收质量等级2的次数 (无)','S4132D:半速率TCH下行接收电平等级3接收质量等级2的次数 (无)','S4133C:半速率TCH上行接收电平等级3接收质量等级3的次数 (无)','S4133D:半速率TCH下行接收电平等级3接收质量等级3的次数 (无)','S4134C:半速率TCH上行接收电平等级3接收质量等级4的次数 (无)','S4134D:半速率TCH下行接收电平等级3接收质量等级4的次数 (无)','S4135C:半速率TCH上行接收电平等级3接收质量等级5的次数 (无)','S4135D:半速率TCH下行接收电平等级3接收质量等级5的次数 (无)','S4136C:半速率TCH上行接收电平等级3接收质量等级6的次数 (无)','S4136D:半速率TCH下行接收电平等级3接收质量等级6的次数 (无)','S4137C:半速率TCH上行接收电平等级3接收质量等级7的次数 (无)','S4137D:半速率TCH下行接收电平等级3接收质量等级7的次数 (无)','S4140C:半速率TCH上行接收电平等级4接收质量等级0的次数 (无)','S4140D:半速率TCH下行接收电平等级4接收质量等级0的次数 (无)','S4141C:半速率TCH上行接收电平等级4接收质量等级1的次数 (无)','S4141D:半速率TCH下行接收电平等级4接收质量等级1的次数 (无)','S4142C:半速率TCH上行接收电平等级4接收质量等级2的次数 (无)','S4142D:半速率TCH下行接收电平等级4接收质量等级2的次数 (无)','S4143C:半速率TCH上行接收电平等级4接收质量等级3的次数 (无)','S4143D:半速率TCH下行接收电平等级4接收质量等级3的次数 (无)','S4144C:半速率TCH上行接收电平等级4接收质量等级4的次数 (无)','S4144D:半速率TCH下行接收电平等级4接收质量等级4的次数 (无)','S4145C:半速率TCH上行接收电平等级4接收质量等级5的次数 (无)','S4145D:半速率TCH下行接收电平等级4接收质量等级5的次数 (无)','S4146C:半速率TCH上行接收电平等级4接收质量等级6的次数 (无)','S4146D:半速率TCH下行接收电平等级4接收质量等级6的次数 (无)','S4147C:半速率TCH上行接收电平等级4接收质量等级7的次数 (无)','S4147D:半速率TCH下行接收电平等级4接收质量等级7的次数 (无)']
h57columns = ['起始时间','周期','网元名称','Cell','TRX','S4150C:半速率TCH上行接收电平等级5接收质量等级0的次数 (无)','S4150D:半速率TCH下行接收电平等级5接收质量等级0的次数 (无)','S4151C:半速率TCH上行接收电平等级5接收质量等级1的次数 (无)','S4151D:半速率TCH下行接收电平等级5接收质量等级1的次数 (无)','S4152C:半速率TCH上行接收电平等级5接收质量等级2的次数 (无)','S4152D:半速率TCH下行接收电平等级5接收质量等级2的次数 (无)','S4153C:半速率TCH上行接收电平等级5接收质量等级3的次数 (无)','S4153D:半速率TCH下行接收电平等级5接收质量等级3的次数 (无)','S4154C:半速率TCH上行接收电平等级5接收质量等级4的次数 (无)','S4154D:半速率TCH下行接收电平等级5接收质量等级4的次数 (无)','S4155C:半速率TCH上行接收电平等级5接收质量等级5的次数 (无)','S4155D:半速率TCH下行接收电平等级5接收质量等级5的次数 (无)','S4156C:半速率TCH上行接收电平等级5接收质量等级6的次数 (无)','S4156D:半速率TCH下行接收电平等级5接收质量等级6的次数 (无)','S4157C:半速率TCH上行接收电平等级5接收质量等级7的次数 (无)','S4157D:半速率TCH下行接收电平等级5接收质量等级7的次数 (无)','S4160C:半速率TCH上行接收电平等级6接收质量等级0的次数 (无)','S4160D:半速率TCH下行接收电平等级6接收质量等级0的次数 (无)','S4161C:半速率TCH上行接收电平等级6接收质量等级1的次数 (无)','S4161D:半速率TCH下行接收电平等级6接收质量等级1的次数 (无)','S4162C:半速率TCH上行接收电平等级6接收质量等级2的次数 (无)','S4162D:半速率TCH下行接收电平等级6接收质量等级2的次数 (无)','S4163C:半速率TCH上行接收电平等级6接收质量等级3的次数 (无)','S4163D:半速率TCH下行接收电平等级6接收质量等级3的次数 (无)','S4164C:半速率TCH上行接收电平等级6接收质量等级4的次数 (无)','S4164D:半速率TCH下行接收电平等级6接收质量等级4的次数 (无)','S4165C:半速率TCH上行接收电平等级6接收质量等级5的次数 (无)','S4165D:半速率TCH下行接收电平等级6接收质量等级5的次数 (无)','S4166C:半速率TCH上行接收电平等级6接收质量等级6的次数 (无)','S4166D:半速率TCH下行接收电平等级6接收质量等级6的次数 (无)','S4167C:半速率TCH上行接收电平等级6接收质量等级7的次数 (无)','S4167D:半速率TCH下行接收电平等级6接收质量等级7的次数 (无)','S4170C:半速率TCH上行接收电平等级7接收质量等级0的次数 (无)','S4170D:半速率TCH下行接收电平等级7接收质量等级0的次数 (无)','S4171C:半速率TCH上行接收电平等级7接收质量等级1的次数 (无)','S4171D:半速率TCH下行接收电平等级7接收质量等级1的次数 (无)','S4172C:半速率TCH上行接收电平等级7接收质量等级2的次数 (无)','S4172D:半速率TCH下行接收电平等级7接收质量等级2的次数 (无)','S4173C:半速率TCH上行接收电平等级7接收质量等级3的次数 (无)','S4173D:半速率TCH下行接收电平等级7接收质量等级3的次数 (无)','S4174C:半速率TCH上行接收电平等级7接收质量等级4的次数 (无)','S4174D:半速率TCH下行接收电平等级7接收质量等级4的次数 (无)','S4175C:半速率TCH上行接收电平等级7接收质量等级5的次数 (无)','S4175D:半速率TCH下行接收电平等级7接收质量等级5的次数 (无)','S4176C:半速率TCH上行接收电平等级7接收质量等级6的次数 (无)','S4176D:半速率TCH下行接收电平等级7接收质量等级6的次数 (无)','S4177C:半速率TCH上行接收电平等级7接收质量等级7的次数 (无)','S4177D:半速率TCH下行接收电平等级7接收质量等级7的次数 (无)']
f04columns = ['起始时间','周期','网元名称','Cell','TRX','S4100A:全速率TCH上行接收电平等级0接收质量等级0的次数 (无)','S4100B:全速率TCH下行接收电平等级0接收质量等级0的次数 (无)','S4101A:全速率TCH上行接收电平等级0接收质量等级1的次数 (无)','S4101B:全速率TCH下行接收电平等级0接收质量等级1的次数 (无)','S4102A:全速率TCH上行接收电平等级0接收质量等级2的次数 (无)','S4102B:全速率TCH下行接收电平等级0接收质量等级2的次数 (无)','S4103A:全速率TCH上行接收电平等级0接收质量等级3的次数 (无)','S4103B:全速率TCH下行接收电平等级0接收质量等级3的次数 (无)','S4104A:全速率TCH上行接收电平等级0接收质量等级4的次数 (无)','S4104B:全速率TCH下行接收电平等级0接收质量等级4的次数 (无)','S4105A:全速率TCH上行接收电平等级0接收质量等级5的次数 (无)','S4105B:全速率TCH下行接收电平等级0接收质量等级5的次数 (无)','S4106A:全速率TCH上行接收电平等级0接收质量等级6的次数 (无)','S4106B:全速率TCH下行接收电平等级0接收质量等级6的次数 (无)','S4107A:全速率TCH上行接收电平等级0接收质量等级7的次数 (无)','S4107B:全速率TCH下行接收电平等级0接收质量等级7的次数 (无)','S4110A:全速率TCH上行接收电平等级1接收质量等级0的次数 (无)','S4110B:全速率TCH下行接收电平等级1接收质量等级0的次数 (无)','S4111A:全速率TCH上行接收电平等级1接收质量等级1的次数 (无)','S4111B:全速率TCH下行接收电平等级1接收质量等级1的次数 (无)','S4112A:全速率TCH上行接收电平等级1接收质量等级2的次数 (无)','S4112B:全速率TCH下行接收电平等级1接收质量等级2的次数 (无)','S4113A:全速率TCH上行接收电平等级1接收质量等级3的次数 (无)','S4113B:全速率TCH下行接收电平等级1接收质量等级3的次数 (无)','S4114A:全速率TCH上行接收电平等级1接收质量等级4的次数 (无)','S4114B:全速率TCH下行接收电平等级1接收质量等级4的次数 (无)','S4115A:全速率TCH上行接收电平等级1接收质量等级5的次数 (无)','S4115B:全速率TCH下行接收电平等级1接收质量等级5的次数 (无)','S4116A:全速率TCH上行接收电平等级1接收质量等级6的次数 (无)','S4116B:全速率TCH下行接收电平等级1接收质量等级6的次数 (无)','S4117A:全速率TCH上行接收电平等级1接收质量等级7的次数 (无)','S4117B:全速率TCH下行接收电平等级1接收质量等级7的次数 (无)','S4120A:全速率TCH上行接收电平等级2接收质量等级0的次数 (无)','S4120B:全速率TCH下行接收电平等级2接收质量等级0的次数 (无)','S4121A:全速率TCH上行接收电平等级2接收质量等级1的次数 (无)','S4121B:全速率TCH下行接收电平等级2接收质量等级1的次数 (无)','S4122A:全速率TCH上行接收电平等级2接收质量等级2的次数 (无)','S4122B:全速率TCH下行接收电平等级2接收质量等级2的次数 (无)','S4123A:全速率TCH上行接收电平等级2接收质量等级3的次数 (无)','S4123B:全速率TCH下行接收电平等级2接收质量等级3的次数 (无)','S4124A:全速率TCH上行接收电平等级2接收质量等级4的次数 (无)','S4124B:全速率TCH下行接收电平等级2接收质量等级4的次数 (无)','S4125A:全速率TCH上行接收电平等级2接收质量等级5的次数 (无)','S4125B:全速率TCH下行接收电平等级2接收质量等级5的次数 (无)','S4126A:全速率TCH上行接收电平等级2接收质量等级6的次数 (无)','S4126B:全速率TCH下行接收电平等级2接收质量等级6的次数 (无)','S4127A:全速率TCH上行接收电平等级2接收质量等级7的次数 (无)','S4127B:全速率TCH下行接收电平等级2接收质量等级7的次数 (无)','S4130A:全速率TCH上行接收电平等级3接收质量等级0的次数 (无)','S4130B:全速率TCH下行接收电平等级3接收质量等级0的次数 (无)','S4131A:全速率TCH上行接收电平等级3接收质量等级1的次数 (无)','S4131B:全速率TCH下行接收电平等级3接收质量等级1的次数 (无)','S4132A:全速率TCH上行接收电平等级3接收质量等级2的次数 (无)','S4132B:全速率TCH下行接收电平等级3接收质量等级2的次数 (无)','S4133A:全速率TCH上行接收电平等级3接收质量等级3的次数 (无)','S4133B:全速率TCH下行接收电平等级3接收质量等级3的次数 (无)','S4134A:全速率TCH上行接收电平等级3接收质量等级4的次数 (无)','S4134B:全速率TCH下行接收电平等级3接收质量等级4的次数 (无)','S4135A:全速率TCH上行接收电平等级3接收质量等级5的次数 (无)','S4135B:全速率TCH下行接收电平等级3接收质量等级5的次数 (无)','S4136A:全速率TCH上行接收电平等级3接收质量等级6的次数 (无)','S4136B:全速率TCH下行接收电平等级3接收质量等级6的次数 (无)','S4137A:全速率TCH上行接收电平等级3接收质量等级7的次数 (无)','S4137B:全速率TCH下行接收电平等级3接收质量等级7的次数 (无)','S4140A:全速率TCH上行接收电平等级4接收质量等级0的次数 (无)','S4140B:全速率TCH下行接收电平等级4接收质量等级0的次数 (无)','S4141A:全速率TCH上行接收电平等级4接收质量等级1的次数 (无)','S4141B:全速率TCH下行接收电平等级4接收质量等级1的次数 (无)','S4142A:全速率TCH上行接收电平等级4接收质量等级2的次数 (无)','S4142B:全速率TCH下行接收电平等级4接收质量等级2的次数 (无)','S4143A:全速率TCH上行接收电平等级4接收质量等级3的次数 (无)','S4143B:全速率TCH下行接收电平等级4接收质量等级3的次数 (无)','S4144A:全速率TCH上行接收电平等级4接收质量等级4的次数 (无)','S4144B:全速率TCH下行接收电平等级4接收质量等级4的次数 (无)','S4145A:全速率TCH上行接收电平等级4接收质量等级5的次数 (无)','S4145B:全速率TCH下行接收电平等级4接收质量等级5的次数 (无)','S4146A:全速率TCH上行接收电平等级4接收质量等级6的次数 (无)','S4146B:全速率TCH下行接收电平等级4接收质量等级6的次数 (无)','S4147A:全速率TCH上行接收电平等级4接收质量等级7的次数 (无)','S4147B:全速率TCH下行接收电平等级4接收质量等级7的次数 (无)']
f57columns = ['起始时间','周期','网元名称','Cell','TRX','S4150A:全速率TCH上行接收电平等级5接收质量等级0的次数 (无)','S4150B:全速率TCH下行接收电平等级5接收质量等级0的次数 (无)','S4151A:全速率TCH上行接收电平等级5接收质量等级1的次数 (无)','S4151B:全速率TCH下行接收电平等级5接收质量等级1的次数 (无)','S4152A:全速率TCH上行接收电平等级5接收质量等级2的次数 (无)','S4152B:全速率TCH下行接收电平等级5接收质量等级2的次数 (无)','S4153A:全速率TCH上行接收电平等级5接收质量等级3的次数 (无)','S4153B:全速率TCH下行接收电平等级5接收质量等级3的次数 (无)','S4154A:全速率TCH上行接收电平等级5接收质量等级4的次数 (无)','S4154B:全速率TCH下行接收电平等级5接收质量等级4的次数 (无)','S4155A:全速率TCH上行接收电平等级5接收质量等级5的次数 (无)','S4155B:全速率TCH下行接收电平等级5接收质量等级5的次数 (无)','S4156A:全速率TCH上行接收电平等级5接收质量等级6的次数 (无)','S4156B:全速率TCH下行接收电平等级5接收质量等级6的次数 (无)','S4157A:全速率TCH上行接收电平等级5接收质量等级7的次数 (无)','S4157B:全速率TCH下行接收电平等级5接收质量等级7的次数 (无)','S4160A:全速率TCH上行接收电平等级6接收质量等级0的次数 (无)','S4160B:全速率TCH下行接收电平等级6接收质量等级0的次数 (无)','S4161A:全速率TCH上行接收电平等级6接收质量等级1的次数 (无)','S4161B:全速率TCH下行接收电平等级6接收质量等级1的次数 (无)','S4162A:全速率TCH上行接收电平等级6接收质量等级2的次数 (无)','S4162B:全速率TCH下行接收电平等级6接收质量等级2的次数 (无)','S4163A:全速率TCH上行接收电平等级6接收质量等级3的次数 (无)','S4163B:全速率TCH下行接收电平等级6接收质量等级3的次数 (无)','S4164A:全速率TCH上行接收电平等级6接收质量等级4的次数 (无)','S4164B:全速率TCH下行接收电平等级6接收质量等级4的次数 (无)','S4165A:全速率TCH上行接收电平等级6接收质量等级5的次数 (无)','S4165B:全速率TCH下行接收电平等级6接收质量等级5的次数 (无)','S4166A:全速率TCH上行接收电平等级6接收质量等级6的次数 (无)','S4166B:全速率TCH下行接收电平等级6接收质量等级6的次数 (无)','S4167A:全速率TCH上行接收电平等级6接收质量等级7的次数 (无)','S4167B:全速率TCH下行接收电平等级6接收质量等级7的次数 (无)','S4170A:全速率TCH上行接收电平等级7接收质量等级0的次数 (无)','S4170B:全速率TCH下行接收电平等级7接收质量等级0的次数 (无)','S4171A:全速率TCH上行接收电平等级7接收质量等级1的次数 (无)','S4171B:全速率TCH下行接收电平等级7接收质量等级1的次数 (无)','S4172A:全速率TCH上行接收电平等级7接收质量等级2的次数 (无)','S4172B:全速率TCH下行接收电平等级7接收质量等级2的次数 (无)','S4173A:全速率TCH上行接收电平等级7接收质量等级3的次数 (无)','S4173B:全速率TCH下行接收电平等级7接收质量等级3的次数 (无)','S4174A:全速率TCH上行接收电平等级7接收质量等级4的次数 (无)','S4174B:全速率TCH下行接收电平等级7接收质量等级4的次数 (无)','S4175A:全速率TCH上行接收电平等级7接收质量等级5的次数 (无)','S4175B:全速率TCH下行接收电平等级7接收质量等级5的次数 (无)','S4176A:全速率TCH上行接收电平等级7接收质量等级6的次数 (无)','S4176B:全速率TCH下行接收电平等级7接收质量等级6的次数 (无)','S4177A:全速率TCH上行接收电平等级7接收质量等级7的次数 (无)','S4177B:全速率TCH下行接收电平等级7接收质量等级7的次数 (无)']
nbcolumns = ["起始时间","周期","网元名称","GCELL_NCELL","BCCH","BCC,NCC","NCC","AS360:邻近小区平均信号强度 (分贝)","AS362:服务小区与邻区信号强度差平均值 (分贝)","S360:邻近小区信号强度 (分贝)","S361:邻近小区测量报告数目 (无)","S362:服务小区信号强度 (分贝)","S363:服务小区与邻区信号强度差小于邻区干扰电平门限1的测量报告数 (无)","S364:服务小区与邻区信号强度差大于邻区干扰电平门限1的测量报告数 (无)","S365:服务小区与邻区信号强度差大于邻区干扰电平门限2的测量报告数 (无)","S366:服务小区与邻区信号强度差大于邻区干扰电平门限3的测量报告数 (无)","S367:服务小区与邻区信号强度差大于邻区干扰电平门限4的测量报告数 (无)","S368:服务小区与邻区信号强度差大于邻区干扰电平门限5的测量报告数 (无)","S369:服务小区与邻区信号强度差大于邻区干扰电平门限6的测量报告数 (无)","S370:服务小区与邻区信号强度差大于邻区干扰电平门限7的测量报告数 (无)","S371:邻区与服务小区信号强度差大于相对电平门限的测量报告数 (无)","S372:邻区信号强度大于绝对电平门限的测量报告数 (无)","S386:竞争小区信号处于电平等级0的次数 (无)","S387:竞争小区信号处于电平等级1的次数 (无)","S388:竞争小区信号处于电平等级2的次数 (无)","S389:竞争小区信号处于电平等级3的次数 (无)","S390:竞争小区信号处于电平等级4的次数 (无)","S391:竞争小区信号处于电平等级5的次数 (无)","S392:竞争小区信号处于电平等级6的次数 (无)","S393:竞争小区信号处于电平等级7的次数 (无)","S394:服务小区与邻区信号强度差小于邻区干扰电平门限0的测量报告数 (无)"]

file_full = "full.csv"
def handle_full(file_full):
	file_full = "full.csv"
	df_full = pd.read_csv(file_full,encoding='gbk',skiprows=7)
	df_full.to_csv("全速率0-4.csv",encoding='gbk',columns=f04columns,index=False,header=True)
	df_full.to_csv("全速率5-7.csv",encoding='gbk',columns=f57columns,index=False,header=True)

new = handle_full(file_full)

file_half = "half.csv"
def handle_half(file_half):
	file_half = "half.csv"
	df_half = pd.read_csv(file_half,encoding='gbk',skiprows=7)
	df_half.to_csv("半速率0-4.csv",encoding='gbk',columns=h04columns,index=False,header=True)
	df_half.to_csv("半速率5-7.csv",encoding='gbk',columns=h57columns,index=False,header=True)

new = handle_full(file_half)


file_nb = "nb.csv"
def handle_nb(file_nb):
	file_nb = "nb.csv"
	df_nb = pd.read_csv(file_nb,encoding='gbk',skiprows=7)
	df_nb.to_csv("邻区测量.csv",encoding='gbk',columns=nbcolumns,index=False,header=True)
	
new = handle_full(file_nb)

单测代码：===== 单文件分拣end



单测代码：===============
import os
def make_folders_test():
	day8digi = ['TEST1']
	bscs = ['bsc1','bsc2','bsc3',]
	currdir = os.path.abspath('.')
	for index in range(len(day8digi)):
			joineddir = os.path.join(currdir,'ms',day8digi[index])
			print(joineddir)
			for index in range(len(bscs)):
				joineddir1 = os.path.join(joineddir,bscs[index])
				print(joineddir1)

make_folders_test()
单测代码：===============


测试代码：
=====================================================
测试代码 处理读取CSV，输出 BSC列表和时间日期的元组，暂不处理dataframe
=====================================================
import os,sys,shutil
import pandas as pd
from datetime import datetime


csv_file = "full.csv"
def read2bscsdtime(csv_file):
	csv_file = "full.csv"
	skip_row = 8
	df = pd.read_csv(csv_file,encoding='gbk',skiprows=skip_row-1)
	dfbsc = df['网元名称']
	dfbsc = dfbsc.drop_duplicates()
	bscs=list(dfbsc)

	dfstarttime = df['起始时间']
	dfstarttime = dfstarttime.drop_duplicates()
	dfstarttime = list(dfstarttime)
	
	return dfstarttime,bscs,df #输出的是元组([day8],[bscs])



read2bscsdtime = read2bscsdtime(csv_file)
测试代码 结束
====


=====================================================
测试代码：开始合并去重多个list
=====================================================

days_nb = ['a','b','c']
days_half =['a','b','c']
days_full = ['a','b','c']

bscs_half =['a','b','c']
bscs_full =['a','b','c']
bscs_nb =['a','b','c']

from itertools import chain
listday = list(set(chain.from_iterable(zip(days_nb, days_half,days_full))))
listbsc = list(set(chain.from_iterable(zip(days_nb, bscs_half,bscs_full))))

=====================================================
测试代码：结束
=====================================================

=====================================================
测试单元2 将起始时间处理成8位数的字符串，BSC无需处理，从元组read2bscsdtime中tp[0],tp[1]提取即可，准备下一步创建目录
=====================================================
