# P112
# 迭代(iteration)：一個接一個，逐一操作。

# P113
a = 22; b = 4+5j; c = 'hi'; d = (169, 44)
e = ['Amy', a, d]
def sq(x): return x * x
import math
# a.b.c.d.e.sq.math為名稱↓↓
# 指向某物件，物件必有某種型別

print(type(a),type(c),type(e))
print(type(sq),type(math))
print('----------------------')

it = type(a)
print(it)
print(type(a) is type(99))
print(int, float, complex)
print(tuple, list, str)
print(type(e) is list)
print('----------------------')

# P114
import types
print(type(sq) is types.FunctionType)
print(type(math) is types.ModuleType)
print('----------------------')

a = 3
print(type(a))
at = type(a)	# at指向type物件
print(type(at))
print('----------------------')

#-----------*---------------------------------------#
#    型別   |          位置         				|
#-----------|---------------------------------------|
#  	bool    |			內建名稱bool    			|
#  	int     |		  	′′  int  					|
#  complex	|		 	′′	complex 				|
#   list	|		  	′′ list						|
#   tuple	| 		  	′′  tuple					|
#   str		|			′′  str						|
#  Function |	module，types.FunctionType			|
#  module   |   module，types.ModuleType   	 		|
# 內建函數	|	module，types.BuiltinFunctionType	|
# 內建方法	|	module，types.BuiltinMethodType		|
# Decimal	|	module，decimal.Decimal				|
# Fraction	|	module，fractions.Fraction			|
# ↑分數		|	------------------------------------|
# 	dict	|			內建名稱dict				|
# 	slice	|			內建名稱slice				|
#	set		|			內建名稱set					|
#---------------------------------------------------#

# P115
# 實體(instance)-->某型別建立出之物件
#	↑----可判斷物件是否為某型別之實體
print(callable(sq), callable(math))
print(callable(list), callable(int))
print(isinstance(sq, types.FunctionType))
print(isinstance(d, tuple))
# sq 為function 可被呼叫
# list、int可被呼叫作為該型別之建構式。
# sq 是函式型別的實體
# d 是tuple 型別的實體
print('----------------------')

# dir():查看某物件有什麼東西，用於互動交談模式下
# 快速查詢有用資訊，但並不完整

print(dir())
print(dir(int))
print(dir(list))
print('----------------------')

# P116	命名空間
import math
pi = math.pi
c = complex(3, 4)
def circle(r):
	area = pi * r * r
	return area
print(c)
print(circle(5))
# math --> module
# pi、c --> 物件
print('----------------------')


# 搜尋名稱順序：
# 區域 -> 全域 -> 內建名稱命名空間(module __builtins__)

# 區域 -- 外圍函式(enclosing function) -- 全域 **
# LEGB(Local、Enclosing、Global、Builtin) **