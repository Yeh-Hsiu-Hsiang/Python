#P021
a = 3   # = 指派
print(a)

#--------------------#

#P022
a = 7
print(a)
b = 1.25    #creat float type
c = 'hello'

#--------------------#

#P024 list
li0 = [30,41,52,63]
print(li0[2])
li1 = ['amy', 'bob', 'cathy']
b = li1[1]
print(b)
# print(li1[99]) 
#Traceback (most recent call last):
#IndexError: list index out of range
#若以n為索引值存取list ↓↓↓ 
#「off-by-one error」(離一錯誤)

#--------------------#

#P025
li2 = [3, 101, 4.56, 'book', 'music']
li3 = ['Frank', 177, 68, 'engineer', ['C', 'Python']]
print(li3[4])
print(li3[4][1])

#--------------------#

#P026 immutable & mutable
a = 3
a = 4   #不可變(immutable)
print(a) 

#*-------------*#

name = 'Frank'
weight = 177
height = 68
title = 'engineer'  #職稱
langs = ['C', 'Python']
li4 = [name, weight, height, title, langs]
li4 [2] = 75    #可變(mutable)
print(li4)

#---------------------------#

#P027 別名(alias):2個以上名稱指向同一物件
a = 3   #不可變
b = a
print(a,b)
b = 4
print(a,b)

#*-------------*#
a = [60, 71, 82]    #可變
b = a
print(a,b)
b[0] = 99
print(a,b)

#---------------------------#
#P028 tuple(元組) --> immutable list
()
print()

t0 = (30, 41, 52, 63)
print(t0[2])

t1 = ('amy', 'bob', 'cathy')
b = t1[1]
print(b)

# t1[0] = 'annie' 
#tuple is immutable , don't write
#Traceback (most recent call last):
#TypeError: 'tuple' object is not callable

# print(t1[99])
#Traceback (most recent call last):
#IndexError: tuple index out of range

#*-------------*#

t0 = (0, 1, 2, 3)
t1 = t0
t1[0] = 99 
print(t1)
#TypeError: 'tuple' object does not support item assignment

#---------------------------#
#P029
t0 = ('only one')   # string type
t1 = ('only one',)  # tuple type
print(('a', 'b', 'c'))
print('a', 'b', 'c')
