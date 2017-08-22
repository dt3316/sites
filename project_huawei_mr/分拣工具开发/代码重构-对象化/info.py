class Programmer(object):
	hobby = 'Playing Computer'

	def __init__(self,name,age,weight):
		self.name = name
		self.age = age
		self.__weight = weight

	def get_weight(self):
		return self.__weight

if __name__ == '__main__':  #直接继承object新式类的__name__都是__main__
	Programmer = Programmer('Albert',25,80)
	print(dir(Programmer))
	print(Programmer.__dict__) # 对象内置的打印全部属性
	print(Programmer.get_weight())
	Programmer._Programmer__weight


try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: 找不到文件或者无法打开")
else:
   print ("Written content in the file successfully")
   fh.close()