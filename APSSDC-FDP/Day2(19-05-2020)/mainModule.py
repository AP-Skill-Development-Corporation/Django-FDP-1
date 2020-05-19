#from packages import myMath
from packages.myMath import Math as mt


#obj = myMath.Math
obj = mt
#print(dir(obj))
print(obj.__doc__)
print(obj.isEven(35))
print(obj.isOdd(57))
bval = int(input("enter base value:"))
pval  = int(input("Enter power val:"))
print(obj.power(bval,pval))
