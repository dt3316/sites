a=10
b=20

#>>> print("{} is bigger than {}" .format(a,b))
#10 is bigger than 20

# >>> print( "%s is %s" %(a,b))
# 10 is 20
# >>>
# >>> print( "%d2 is %d2" %(a,b))
# 102 is 202
# >>> print( "%d is %d" %(a,b))
# 10 is 20
import os,glob
os.chdir('/Users/dongtao')
for file in glob.glob("*.txt"):
    print(file)

#README.txt
import os
import sys
print(sys.executable)
