# P089 Bool
print(bool)
print(type(True) is bool, type(False) is bool)
print('---------------------')

print(True is 1, False is 0)
print(True == 1, False == 0)
print(3 + True, False - 3)
print('---------------------')

# P090
x, y, z = 3, 5, 7
print(x if y > 0 else z)
print(x if y < 0 else z)
d = 100; n = None
n = d if n is False or n is None else n # 若None，d為預設值
n = d if n else n
print('---------------------')

# P091
x, y, z = 3, 5, 7
print((y > 0 and x) or z)
print((y < 0 and x) or z)
d = 100; n = None
n0 = d if n == None else n #if n ==None then n0 = d
n1 = (n == None) and d or n
n2 = (n and d ) or n
print(n0, n1, n2)
print('---------------------')
# 相同功能但較簡潔的語法稱為「語法糖(syntactic sugar)」
