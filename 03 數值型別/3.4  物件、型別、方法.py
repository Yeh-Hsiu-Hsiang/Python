# P091
print(3 + 5, 'Hello' + 'Python')
a = [0, 1, 2]; b ='hello'
print(len(a), len(b))
print('----------------')

li = [0, 1, 2]
print(li.__len__()) #__len__() list中得知長度
li.append(3)
print(li)
print('----------------')

# P092
# 運算子&內建函數視同「方法(method)」的語法糖
# 當直譯器看到運算子&內建函式時會轉成方法的呼叫
# 方法附屬於某型別之物件
# 呼叫方法：物件.方法(參數)--->(參數)代表呼叫
# ex: li.append(3)

x = 'Good'; y = 'Morning'
print(x + y)
x.__add__(y)
print(x)
x = 3; y = 4
print(x + y)
print(x.__add__(y))
print(x.__add__(y).__sub__(y.__pow__(2)))
print('----------------')