# P096
# print('hello' + 5)
# TypeError:
# Can't convert 'int' object to str implicitly

print('hello' + str(5))
print(int('99') + 6)
print(int(3.14))
print('------------------')
# print(int(5 + 4j))  # 複數無法轉整數**
# TypeError: can't convert complex to int

print('hello'); print(3); print(3.14); print(4+5j)
a = 3
print(a.__str__())
print('------------------')

# __repr__ & __str__ 皆是回傳字串**
# repr 可當程式碼， str 方便讀懂**

# P097
z = 4 + 5j
print(z.__str__(), z.__repr__())

from decimal import *
d = Decimal('3.1415926')
print(d.__str__())
print(d.__repr__())
print(d)
print('------------------')