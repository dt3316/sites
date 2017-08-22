# encoding:utf-8

import sys
# print(sys.executable)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']
           }
result = student['name']
result = student['courses']


# 键key可以是整数，也可以是文本，也可以是个变量

result = student.keys()
result = student.values()

student['phone'] = '555-1234'
student['name'] = 'Jane'

print(result)
