#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding:utf-8 -*- 
import os,sys,shutil
from os.path import join, getsize
import pandas as pd


def move_files():
	file1 = "./input/half.csv"
	file2 = "./input/full.csv"
	file3 = "./input/nb.csv"
	check_filename1 = input("确认“全速率”命名为“full.csv”(y or n)：")
	check_filename2 = input("请确“半速率”命名为“half.csv”(y or n)：")
	check_filename3 = input("请确“邻区测量”命名为“nb.csv”(y or n)：")
	check_folder = input("请确以上3个文件已经放入input文件夹(y or n)：")

	skip_rows=input("请输入csv的标题行从第__行开始(1 或 8)：")
	skips=int(skip_rows)
	print("==========开始进行分拣，大约需要120秒，请耐心等待==========")
	df1 = pd.read_csv(file1,encoding='gbk',skiprows=skips-1)
	df2 = pd.read_csv(file2,encoding='gbk',skiprows=skips-1)
	df3 = pd.read_csv(file3,encoding='gbk',skiprows=skips-1)
	df1x = df1['网元名称']
	df1x = df1x.drop_duplicates()
	bscs=list(df1x)
	#print('==BSC==',bscs)
	h04header = ['起始时间','周期','网元名称','Cell','TRX','S4100C:半速率TCH上行接收电平等级0接收质量等级0的次数 (无)','S4100D:半速率TCH下行接收电平等级0接收质量等级0的次数 (无)','S4101C:半速率TCH上行接收电平等级0接收质量等级1的次数 (无)','S4101D:半速率TCH下行接收电平等级0接收质量等级1的次数 (无)','S4102C:半速率TCH上行接收电平等级0接收质量等级2的次数 (无)','S4102D:半速率TCH下行接收电平等级0接收质量等级2的次数 (无)','S4103C:半速率TCH上行接收电平等级0接收质量等级3的次数 (无)','S4103D:半速率TCH下行接收电平等级0接收质量等级3的次数 (无)','S4104C:半速率TCH上行接收电平等级0接收质量等级4的次数 (无)','S4104D:半速率TCH下行接收电平等级0接收质量等级4的次数 (无)','S4105C:半速率TCH上行接收电平等级0接收质量等级5的次数 (无)','S4105D:半速率TCH下行接收电平等级0接收质量等级5的次数 (无)','S4106C:半速率TCH上行接收电平等级0接收质量等级6的次数 (无)','S4106D:半速率TCH下行接收电平等级0接收质量等级6的次数 (无)','S4107C:半速率TCH上行接收电平等级0接收质量等级7的次数 (无)','S4107D:半速率TCH下行接收电平等级0接收质量等级7的次数 (无)','S4110C:半速率TCH上行接收电平等级1接收质量等级0的次数 (无)','S4110D:半速率TCH下行接收电平等级1接收质量等级0的次数 (无)','S4111C:半速率TCH上行接收电平等级1接收质量等级1的次数 (无)','S4111D:半速率TCH下行接收电平等级1接收质量等级1的次数 (无)','S4112C:半速率TCH上行接收电平等级1接收质量等级2的次数 (无)','S4112D:半速率TCH下行接收电平等级1接收质量等级2的次数 (无)','S4113C:半速率TCH上行接收电平等级1接收质量等级3的次数 (无)','S4113D:半速率TCH下行接收电平等级1接收质量等级3的次数 (无)','S4114C:半速率TCH上行接收电平等级1接收质量等级4的次数 (无)','S4114D:半速率TCH下行接收电平等级1接收质量等级4的次数 (无)','S4115C:半速率TCH上行接收电平等级1接收质量等级5的次数 (无)','S4115D:半速率TCH下行接收电平等级1接收质量等级5的次数 (无)','S4116C:半速率TCH上行接收电平等级1接收质量等级6的次数 (无)','S4116D:半速率TCH下行接收电平等级1接收质量等级6的次数 (无)','S4117C:半速率TCH上行接收电平等级1接收质量等级7的次数 (无)','S4117D:半速率TCH下行接收电平等级1接收质量等级7的次数 (无)','S4120C:半速率TCH上行接收电平等级2接收质量等级0的次数 (无)','S4120D:半速率TCH下行接收电平等级2接收质量等级0的次数 (无)','S4121C:半速率TCH上行接收电平等级2接收质量等级1的次数 (无)','S4121D:半速率TCH下行接收电平等级2接收质量等级1的次数 (无)','S4122C:半速率TCH上行接收电平等级2接收质量等级2的次数 (无)','S4122D:半速率TCH下行接收电平等级2接收质量等级2的次数 (无)','S4123C:半速率TCH上行接收电平等级2接收质量等级3的次数 (无)','S4123D:半速率TCH下行接收电平等级2接收质量等级3的次数 (无)','S4124C:半速率TCH上行接收电平等级2接收质量等级4的次数 (无)','S4124D:半速率TCH下行接收电平等级2接收质量等级4的次数 (无)','S4125C:半速率TCH上行接收电平等级2接收质量等级5的次数 (无)','S4125D:半速率TCH下行接收电平等级2接收质量等级5的次数 (无)','S4126C:半速率TCH上行接收电平等级2接收质量等级6的次数 (无)','S4126D:半速率TCH下行接收电平等级2接收质量等级6的次数 (无)','S4127C:半速率TCH上行接收电平等级2接收质量等级7的次数 (无)','S4127D:半速率TCH下行接收电平等级2接收质量等级7的次数 (无)','S4130C:半速率TCH上行接收电平等级3接收质量等级0的次数 (无)','S4130D:半速率TCH下行接收电平等级3接收质量等级0的次数 (无)','S4131C:半速率TCH上行接收电平等级3接收质量等级1的次数 (无)','S4131D:半速率TCH下行接收电平等级3接收质量等级1的次数 (无)','S4132C:半速率TCH上行接收电平等级3接收质量等级2的次数 (无)','S4132D:半速率TCH下行接收电平等级3接收质量等级2的次数 (无)','S4133C:半速率TCH上行接收电平等级3接收质量等级3的次数 (无)','S4133D:半速率TCH下行接收电平等级3接收质量等级3的次数 (无)','S4134C:半速率TCH上行接收电平等级3接收质量等级4的次数 (无)','S4134D:半速率TCH下行接收电平等级3接收质量等级4的次数 (无)','S4135C:半速率TCH上行接收电平等级3接收质量等级5的次数 (无)','S4135D:半速率TCH下行接收电平等级3接收质量等级5的次数 (无)','S4136C:半速率TCH上行接收电平等级3接收质量等级6的次数 (无)','S4136D:半速率TCH下行接收电平等级3接收质量等级6的次数 (无)','S4137C:半速率TCH上行接收电平等级3接收质量等级7的次数 (无)','S4137D:半速率TCH下行接收电平等级3接收质量等级7的次数 (无)','S4140C:半速率TCH上行接收电平等级4接收质量等级0的次数 (无)','S4140D:半速率TCH下行接收电平等级4接收质量等级0的次数 (无)','S4141C:半速率TCH上行接收电平等级4接收质量等级1的次数 (无)','S4141D:半速率TCH下行接收电平等级4接收质量等级1的次数 (无)','S4142C:半速率TCH上行接收电平等级4接收质量等级2的次数 (无)','S4142D:半速率TCH下行接收电平等级4接收质量等级2的次数 (无)','S4143C:半速率TCH上行接收电平等级4接收质量等级3的次数 (无)','S4143D:半速率TCH下行接收电平等级4接收质量等级3的次数 (无)','S4144C:半速率TCH上行接收电平等级4接收质量等级4的次数 (无)','S4144D:半速率TCH下行接收电平等级4接收质量等级4的次数 (无)','S4145C:半速率TCH上行接收电平等级4接收质量等级5的次数 (无)','S4145D:半速率TCH下行接收电平等级4接收质量等级5的次数 (无)','S4146C:半速率TCH上行接收电平等级4接收质量等级6的次数 (无)','S4146D:半速率TCH下行接收电平等级4接收质量等级6的次数 (无)','S4147C:半速率TCH上行接收电平等级4接收质量等级7的次数 (无)','S4147D:半速率TCH下行接收电平等级4接收质量等级7的次数 (无)']
	h57header = ['起始时间','周期','网元名称','Cell','TRX','S4150C:半速率TCH上行接收电平等级5接收质量等级0的次数 (无)','S4150D:半速率TCH下行接收电平等级5接收质量等级0的次数 (无)','S4151C:半速率TCH上行接收电平等级5接收质量等级1的次数 (无)','S4151D:半速率TCH下行接收电平等级5接收质量等级1的次数 (无)','S4152C:半速率TCH上行接收电平等级5接收质量等级2的次数 (无)','S4152D:半速率TCH下行接收电平等级5接收质量等级2的次数 (无)','S4153C:半速率TCH上行接收电平等级5接收质量等级3的次数 (无)','S4153D:半速率TCH下行接收电平等级5接收质量等级3的次数 (无)','S4154C:半速率TCH上行接收电平等级5接收质量等级4的次数 (无)','S4154D:半速率TCH下行接收电平等级5接收质量等级4的次数 (无)','S4155C:半速率TCH上行接收电平等级5接收质量等级5的次数 (无)','S4155D:半速率TCH下行接收电平等级5接收质量等级5的次数 (无)','S4156C:半速率TCH上行接收电平等级5接收质量等级6的次数 (无)','S4156D:半速率TCH下行接收电平等级5接收质量等级6的次数 (无)','S4157C:半速率TCH上行接收电平等级5接收质量等级7的次数 (无)','S4157D:半速率TCH下行接收电平等级5接收质量等级7的次数 (无)','S4160C:半速率TCH上行接收电平等级6接收质量等级0的次数 (无)','S4160D:半速率TCH下行接收电平等级6接收质量等级0的次数 (无)','S4161C:半速率TCH上行接收电平等级6接收质量等级1的次数 (无)','S4161D:半速率TCH下行接收电平等级6接收质量等级1的次数 (无)','S4162C:半速率TCH上行接收电平等级6接收质量等级2的次数 (无)','S4162D:半速率TCH下行接收电平等级6接收质量等级2的次数 (无)','S4163C:半速率TCH上行接收电平等级6接收质量等级3的次数 (无)','S4163D:半速率TCH下行接收电平等级6接收质量等级3的次数 (无)','S4164C:半速率TCH上行接收电平等级6接收质量等级4的次数 (无)','S4164D:半速率TCH下行接收电平等级6接收质量等级4的次数 (无)','S4165C:半速率TCH上行接收电平等级6接收质量等级5的次数 (无)','S4165D:半速率TCH下行接收电平等级6接收质量等级5的次数 (无)','S4166C:半速率TCH上行接收电平等级6接收质量等级6的次数 (无)','S4166D:半速率TCH下行接收电平等级6接收质量等级6的次数 (无)','S4167C:半速率TCH上行接收电平等级6接收质量等级7的次数 (无)','S4167D:半速率TCH下行接收电平等级6接收质量等级7的次数 (无)','S4170C:半速率TCH上行接收电平等级7接收质量等级0的次数 (无)','S4170D:半速率TCH下行接收电平等级7接收质量等级0的次数 (无)','S4171C:半速率TCH上行接收电平等级7接收质量等级1的次数 (无)','S4171D:半速率TCH下行接收电平等级7接收质量等级1的次数 (无)','S4172C:半速率TCH上行接收电平等级7接收质量等级2的次数 (无)','S4172D:半速率TCH下行接收电平等级7接收质量等级2的次数 (无)','S4173C:半速率TCH上行接收电平等级7接收质量等级3的次数 (无)','S4173D:半速率TCH下行接收电平等级7接收质量等级3的次数 (无)','S4174C:半速率TCH上行接收电平等级7接收质量等级4的次数 (无)','S4174D:半速率TCH下行接收电平等级7接收质量等级4的次数 (无)','S4175C:半速率TCH上行接收电平等级7接收质量等级5的次数 (无)','S4175D:半速率TCH下行接收电平等级7接收质量等级5的次数 (无)','S4176C:半速率TCH上行接收电平等级7接收质量等级6的次数 (无)','S4176D:半速率TCH下行接收电平等级7接收质量等级6的次数 (无)','S4177C:半速率TCH上行接收电平等级7接收质量等级7的次数 (无)','S4177D:半速率TCH下行接收电平等级7接收质量等级7的次数 (无)']
	f04header = ['起始时间','周期','网元名称','Cell','TRX','S4100A:全速率TCH上行接收电平等级0接收质量等级0的次数 (无)','S4100B:全速率TCH下行接收电平等级0接收质量等级0的次数 (无)','S4101A:全速率TCH上行接收电平等级0接收质量等级1的次数 (无)','S4101B:全速率TCH下行接收电平等级0接收质量等级1的次数 (无)','S4102A:全速率TCH上行接收电平等级0接收质量等级2的次数 (无)','S4102B:全速率TCH下行接收电平等级0接收质量等级2的次数 (无)','S4103A:全速率TCH上行接收电平等级0接收质量等级3的次数 (无)','S4103B:全速率TCH下行接收电平等级0接收质量等级3的次数 (无)','S4104A:全速率TCH上行接收电平等级0接收质量等级4的次数 (无)','S4104B:全速率TCH下行接收电平等级0接收质量等级4的次数 (无)','S4105A:全速率TCH上行接收电平等级0接收质量等级5的次数 (无)','S4105B:全速率TCH下行接收电平等级0接收质量等级5的次数 (无)','S4106A:全速率TCH上行接收电平等级0接收质量等级6的次数 (无)','S4106B:全速率TCH下行接收电平等级0接收质量等级6的次数 (无)','S4107A:全速率TCH上行接收电平等级0接收质量等级7的次数 (无)','S4107B:全速率TCH下行接收电平等级0接收质量等级7的次数 (无)','S4110A:全速率TCH上行接收电平等级1接收质量等级0的次数 (无)','S4110B:全速率TCH下行接收电平等级1接收质量等级0的次数 (无)','S4111A:全速率TCH上行接收电平等级1接收质量等级1的次数 (无)','S4111B:全速率TCH下行接收电平等级1接收质量等级1的次数 (无)','S4112A:全速率TCH上行接收电平等级1接收质量等级2的次数 (无)','S4112B:全速率TCH下行接收电平等级1接收质量等级2的次数 (无)','S4113A:全速率TCH上行接收电平等级1接收质量等级3的次数 (无)','S4113B:全速率TCH下行接收电平等级1接收质量等级3的次数 (无)','S4114A:全速率TCH上行接收电平等级1接收质量等级4的次数 (无)','S4114B:全速率TCH下行接收电平等级1接收质量等级4的次数 (无)','S4115A:全速率TCH上行接收电平等级1接收质量等级5的次数 (无)','S4115B:全速率TCH下行接收电平等级1接收质量等级5的次数 (无)','S4116A:全速率TCH上行接收电平等级1接收质量等级6的次数 (无)','S4116B:全速率TCH下行接收电平等级1接收质量等级6的次数 (无)','S4117A:全速率TCH上行接收电平等级1接收质量等级7的次数 (无)','S4117B:全速率TCH下行接收电平等级1接收质量等级7的次数 (无)','S4120A:全速率TCH上行接收电平等级2接收质量等级0的次数 (无)','S4120B:全速率TCH下行接收电平等级2接收质量等级0的次数 (无)','S4121A:全速率TCH上行接收电平等级2接收质量等级1的次数 (无)','S4121B:全速率TCH下行接收电平等级2接收质量等级1的次数 (无)','S4122A:全速率TCH上行接收电平等级2接收质量等级2的次数 (无)','S4122B:全速率TCH下行接收电平等级2接收质量等级2的次数 (无)','S4123A:全速率TCH上行接收电平等级2接收质量等级3的次数 (无)','S4123B:全速率TCH下行接收电平等级2接收质量等级3的次数 (无)','S4124A:全速率TCH上行接收电平等级2接收质量等级4的次数 (无)','S4124B:全速率TCH下行接收电平等级2接收质量等级4的次数 (无)','S4125A:全速率TCH上行接收电平等级2接收质量等级5的次数 (无)','S4125B:全速率TCH下行接收电平等级2接收质量等级5的次数 (无)','S4126A:全速率TCH上行接收电平等级2接收质量等级6的次数 (无)','S4126B:全速率TCH下行接收电平等级2接收质量等级6的次数 (无)','S4127A:全速率TCH上行接收电平等级2接收质量等级7的次数 (无)','S4127B:全速率TCH下行接收电平等级2接收质量等级7的次数 (无)','S4130A:全速率TCH上行接收电平等级3接收质量等级0的次数 (无)','S4130B:全速率TCH下行接收电平等级3接收质量等级0的次数 (无)','S4131A:全速率TCH上行接收电平等级3接收质量等级1的次数 (无)','S4131B:全速率TCH下行接收电平等级3接收质量等级1的次数 (无)','S4132A:全速率TCH上行接收电平等级3接收质量等级2的次数 (无)','S4132B:全速率TCH下行接收电平等级3接收质量等级2的次数 (无)','S4133A:全速率TCH上行接收电平等级3接收质量等级3的次数 (无)','S4133B:全速率TCH下行接收电平等级3接收质量等级3的次数 (无)','S4134A:全速率TCH上行接收电平等级3接收质量等级4的次数 (无)','S4134B:全速率TCH下行接收电平等级3接收质量等级4的次数 (无)','S4135A:全速率TCH上行接收电平等级3接收质量等级5的次数 (无)','S4135B:全速率TCH下行接收电平等级3接收质量等级5的次数 (无)','S4136A:全速率TCH上行接收电平等级3接收质量等级6的次数 (无)','S4136B:全速率TCH下行接收电平等级3接收质量等级6的次数 (无)','S4137A:全速率TCH上行接收电平等级3接收质量等级7的次数 (无)','S4137B:全速率TCH下行接收电平等级3接收质量等级7的次数 (无)','S4140A:全速率TCH上行接收电平等级4接收质量等级0的次数 (无)','S4140B:全速率TCH下行接收电平等级4接收质量等级0的次数 (无)','S4141A:全速率TCH上行接收电平等级4接收质量等级1的次数 (无)','S4141B:全速率TCH下行接收电平等级4接收质量等级1的次数 (无)','S4142A:全速率TCH上行接收电平等级4接收质量等级2的次数 (无)','S4142B:全速率TCH下行接收电平等级4接收质量等级2的次数 (无)','S4143A:全速率TCH上行接收电平等级4接收质量等级3的次数 (无)','S4143B:全速率TCH下行接收电平等级4接收质量等级3的次数 (无)','S4144A:全速率TCH上行接收电平等级4接收质量等级4的次数 (无)','S4144B:全速率TCH下行接收电平等级4接收质量等级4的次数 (无)','S4145A:全速率TCH上行接收电平等级4接收质量等级5的次数 (无)','S4145B:全速率TCH下行接收电平等级4接收质量等级5的次数 (无)','S4146A:全速率TCH上行接收电平等级4接收质量等级6的次数 (无)','S4146B:全速率TCH下行接收电平等级4接收质量等级6的次数 (无)','S4147A:全速率TCH上行接收电平等级4接收质量等级7的次数 (无)','S4147B:全速率TCH下行接收电平等级4接收质量等级7的次数 (无)']
	f57header = ['起始时间','周期','网元名称','Cell','TRX','S4150A:全速率TCH上行接收电平等级5接收质量等级0的次数 (无)','S4150B:全速率TCH下行接收电平等级5接收质量等级0的次数 (无)','S4151A:全速率TCH上行接收电平等级5接收质量等级1的次数 (无)','S4151B:全速率TCH下行接收电平等级5接收质量等级1的次数 (无)','S4152A:全速率TCH上行接收电平等级5接收质量等级2的次数 (无)','S4152B:全速率TCH下行接收电平等级5接收质量等级2的次数 (无)','S4153A:全速率TCH上行接收电平等级5接收质量等级3的次数 (无)','S4153B:全速率TCH下行接收电平等级5接收质量等级3的次数 (无)','S4154A:全速率TCH上行接收电平等级5接收质量等级4的次数 (无)','S4154B:全速率TCH下行接收电平等级5接收质量等级4的次数 (无)','S4155A:全速率TCH上行接收电平等级5接收质量等级5的次数 (无)','S4155B:全速率TCH下行接收电平等级5接收质量等级5的次数 (无)','S4156A:全速率TCH上行接收电平等级5接收质量等级6的次数 (无)','S4156B:全速率TCH下行接收电平等级5接收质量等级6的次数 (无)','S4157A:全速率TCH上行接收电平等级5接收质量等级7的次数 (无)','S4157B:全速率TCH下行接收电平等级5接收质量等级7的次数 (无)','S4160A:全速率TCH上行接收电平等级6接收质量等级0的次数 (无)','S4160B:全速率TCH下行接收电平等级6接收质量等级0的次数 (无)','S4161A:全速率TCH上行接收电平等级6接收质量等级1的次数 (无)','S4161B:全速率TCH下行接收电平等级6接收质量等级1的次数 (无)','S4162A:全速率TCH上行接收电平等级6接收质量等级2的次数 (无)','S4162B:全速率TCH下行接收电平等级6接收质量等级2的次数 (无)','S4163A:全速率TCH上行接收电平等级6接收质量等级3的次数 (无)','S4163B:全速率TCH下行接收电平等级6接收质量等级3的次数 (无)','S4164A:全速率TCH上行接收电平等级6接收质量等级4的次数 (无)','S4164B:全速率TCH下行接收电平等级6接收质量等级4的次数 (无)','S4165A:全速率TCH上行接收电平等级6接收质量等级5的次数 (无)','S4165B:全速率TCH下行接收电平等级6接收质量等级5的次数 (无)','S4166A:全速率TCH上行接收电平等级6接收质量等级6的次数 (无)','S4166B:全速率TCH下行接收电平等级6接收质量等级6的次数 (无)','S4167A:全速率TCH上行接收电平等级6接收质量等级7的次数 (无)','S4167B:全速率TCH下行接收电平等级6接收质量等级7的次数 (无)','S4170A:全速率TCH上行接收电平等级7接收质量等级0的次数 (无)','S4170B:全速率TCH下行接收电平等级7接收质量等级0的次数 (无)','S4171A:全速率TCH上行接收电平等级7接收质量等级1的次数 (无)','S4171B:全速率TCH下行接收电平等级7接收质量等级1的次数 (无)','S4172A:全速率TCH上行接收电平等级7接收质量等级2的次数 (无)','S4172B:全速率TCH下行接收电平等级7接收质量等级2的次数 (无)','S4173A:全速率TCH上行接收电平等级7接收质量等级3的次数 (无)','S4173B:全速率TCH下行接收电平等级7接收质量等级3的次数 (无)','S4174A:全速率TCH上行接收电平等级7接收质量等级4的次数 (无)','S4174B:全速率TCH下行接收电平等级7接收质量等级4的次数 (无)','S4175A:全速率TCH上行接收电平等级7接收质量等级5的次数 (无)','S4175B:全速率TCH下行接收电平等级7接收质量等级5的次数 (无)','S4176A:全速率TCH上行接收电平等级7接收质量等级6的次数 (无)','S4176B:全速率TCH下行接收电平等级7接收质量等级6的次数 (无)','S4177A:全速率TCH上行接收电平等级7接收质量等级7的次数 (无)','S4177B:全速率TCH下行接收电平等级7接收质量等级7的次数 (无)']
	nbheader = ["起始时间","周期","网元名称","GCELL_NCELL","BCCH","BCC,NCC","NCC","AS360:邻近小区平均信号强度 (分贝)","AS362:服务小区与邻区信号强度差平均值 (分贝)","S360:邻近小区信号强度 (分贝)","S361:邻近小区测量报告数目 (无)","S362:服务小区信号强度 (分贝)","S363:服务小区与邻区信号强度差小于邻区干扰电平门限1的测量报告数 (无)","S364:服务小区与邻区信号强度差大于邻区干扰电平门限1的测量报告数 (无)","S365:服务小区与邻区信号强度差大于邻区干扰电平门限2的测量报告数 (无)","S366:服务小区与邻区信号强度差大于邻区干扰电平门限3的测量报告数 (无)","S367:服务小区与邻区信号强度差大于邻区干扰电平门限4的测量报告数 (无)","S368:服务小区与邻区信号强度差大于邻区干扰电平门限5的测量报告数 (无)","S369:服务小区与邻区信号强度差大于邻区干扰电平门限6的测量报告数 (无)","S370:服务小区与邻区信号强度差大于邻区干扰电平门限7的测量报告数 (无)","S371:邻区与服务小区信号强度差大于相对电平门限的测量报告数 (无)","S372:邻区信号强度大于绝对电平门限的测量报告数 (无)","S386:竞争小区信号处于电平等级0的次数 (无)","S387:竞争小区信号处于电平等级1的次数 (无)","S388:竞争小区信号处于电平等级2的次数 (无)","S389:竞争小区信号处于电平等级3的次数 (无)","S390:竞争小区信号处于电平等级4的次数 (无)","S391:竞争小区信号处于电平等级5的次数 (无)","S392:竞争小区信号处于电平等级6的次数 (无)","S393:竞争小区信号处于电平等级7的次数 (无)","S394:服务小区与邻区信号强度差小于邻区干扰电平门限0的测量报告数 (无)"]
	
	for index in range(len(bscs)):
		print ('======为:', bscs[index],' 创建了目录，并放入5个文件======')
		bscpath1 = "./out/" + bscs[index] +"/"
		os.mkdir(bscpath1)
		df1xx = df1[df1['网元名称']==bscs[index]] #按照BSC筛选
		outfile1x1 = bscpath1+"半速率0-4.csv"
		outfile1x2 = bscpath1+"半速率5-7.csv"
		df1xx.to_csv(outfile1x1,encoding='gbk',columns=h04header,index=False,header=True)
		df1xx.to_csv(outfile1x2,encoding='gbk',columns=h57header,index=False,header=True)
		
		df2xx = df2[df2['网元名称']==bscs[index]] #按照BSC筛选
		outfile2x1 = bscpath1+"全速率0-4.csv"
		outfile2x2 = bscpath1+"全速率5-7.csv"
		df2xx.to_csv(outfile2x1,encoding='gbk',columns=f04header,index=False,header=True)
		df2xx.to_csv(outfile2x2,encoding='gbk',columns=f57header,index=False,header=True)

		df3xx = df3[df3['网元名称']==bscs[index]] #按照BSC筛选
		outfile3xx = bscpath1+"邻区测量.csv"
		df3xx.to_csv(outfile3xx,encoding='gbk',columns=nbheader,index=False,header=True)
		

def create_out_folder():
	out_folder = './out/'
	if os.path.exists(out_folder):
		shutil.rmtree(out_folder)
		print("....................................")
	else:
		print("....................................")
	os.mkdir(out_folder)




def main():
	print("===========欢迎使用湖北移动“华为MR分拣工具”===========")
	print("===========请先确认文件命名及目录后，再执行===========")
	if 1 :
		create_out_folder()
		move_files()





if __name__ == '__main__':
	main()
	print("========华为MR已经分拣到各BSC文件夹中========")
	print("========湖北移动自主清频小组2017年4月========")
	