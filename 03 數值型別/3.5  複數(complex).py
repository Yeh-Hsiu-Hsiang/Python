# P093 複數(complex)
# 型別complex由實部(real part) & 
# 虛部(imaginary part) 所組成

print(3 + 4j)
print(3.45 + 67.89J)
print(5j)
print('-------------')
# j & J 代表虛部**

print(complex())
print(complex(5))
print(complex(5, 6))
print(complex(9 + 9j, 2 + 2j))
print(complex('5-6j'))
# print(complex('5 - 6j')) 
# 不可有空格，字串格式錯誤
print('-------------')
# ValueError:
# complex() arg is a malformed string


# P094
z = 4 + 5j
print(z.real)
print(z.imag)
print(z == z.real + (z.imag * 1j)) 
# 複數由實部與虛部組成**
print(z.conjugate()) # 共軛複數
print('-------------')

# real --> 取實部，為屬性項(attribute)**
# imag --> 取虛部，同上 **
# conjugate 指向方法(附屬某物件函式)**
# 複數不支援運算子『// & %』、內建函式divmod **

x = 4 + 5j; y = 6 +7j
print(x + y, x - y)
print(x * y)
print(x / y)
print(x ** y)
print(pow(x, y))    # 幕次方
print(abs(x))   # 絕對值
print(x == y, x != y)
# print(x < y)
# TypeError:
# unorderable types: complex() < complex()
print('-------------')