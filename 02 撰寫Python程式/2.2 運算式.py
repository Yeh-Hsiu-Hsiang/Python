#P29~P30
a = 3 + 5
b = 6 - 20
c = 200 + a * b
c2 = (200 + a) * b
d = 17 / 3
d2 = 17 // 3 #地板除法(floor division)
e = 17 % 3
f = 2 ** 5
g = +f
h = -f
print(a,b,c,c2)
print(d,d2,e,f)
print(g,h)
print('*------*')
# **地板除法(floor division): <最靠近之數字**

#--------------------#

#P32
x = 17
y = -3
print(x % y)
print(x - (x//y) * y)
print('*------*')
# **{** -> +-(正負號) -> * / // % -> +- }**

print(2 + 3 -1)
print(2 * (3 * 4))
print(2 ** 3 ** 2)
print(2 ** (3 ** 2))
print((2 ** 3) ** 2)
print('*------*')
#*------*#

print('Hello' + ' ' + 'Python' )
print('Hello' * 4) #first copy then link
print(4 * 'Hello')

#--------------------#

#P033
print([0, 1, 2] + [3, 4, 5])
print((0, 1, 2) * 3) 
print('*------*')

#運算子比較 
a = 11
b = 23
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)
#a <> b 2.x版
print('*------*')

#--------------------#
#P34

li0 = [0, 1, 2]
li1 = [3, 4, 5]
li2 = [0] + [1, 2]
print(li0)
print(li0  == li2)
print('*------*')

a = 4
b = 11
li = [2, 3, 5, 7, 11, 13, 17, 19]
t = [0, 2, 4, 6, 8, 10]
print(a in li)
print(b in li)
print(a not in t)
print(b not in t)
print('*------*')

s0 = 'you'
s1 = 'she'
s2 = 'How are you?'
print(s0 in s2)
print(s1 in s2)
print('*------*')

a = 3
b = 4
c = 1 + 2
print(a is b)
print(a == c)
print(a is c)
print('*------*')

t0 = (0, 1, 2)
t1 = t0
t2 = (0, ) + (1, 2)
print(t0 is t1)
print(t0 == t2)
print(t0 is t2)
print('*------*')
#   == 比較兩個物件內容是否相等 **
#   in、not in 是否位於(存在)容器物件內 **
#   is 判別是否為同一物件(指向同一個物件) **

#--------------------#
#P035 邏輯運算子
x = 42
print(0 <= x and x <= 100)
print('*------*')

y = 25
z = 36
a = x < y or z < x
print(a)
print(not a)
print('*------*')

#   None、0、''、list[]、tuple() 都會被當作False **
#   '0'、[0]、tuple(0, ) 皆為True **

li0 = [0, 1, 2]
li1 = []
li2 = [None, False]
print(li0 and li1)
print(li0 or li2)
print('*------*')

li0 = []
li1 = [30, 41, 52]
print(li0 and li0[0] > 25)
print(li1 and li1[0] > 25)
print([] or '0')
print('' or [0] or () or 0)
print('*------*')
# or --> 當True & False 同時存在時，執行True

#運算子優先順序
#  1 (expr..)、[expr..]、{key:value..}(字典)、{expr..}(集合)
#  2 x[index]、x[index:index](切片)、
#   x(arguments..)(函式呼叫)、x.attribute(屬性向存取)
#  3 **
#  4 +x、-x、~x(位元運算NOT)
#  5 *、/、//、%
#  6 +、-
#  7 <<、>>(位元位移運算)
#  8 &、^(XOR)、|(or)
#  9 in、not in、is、is not、<、<=、>、>=、!=、==
#  10 not x、 and 、 or(布林邏輯運算)
#  11 if/else
#  12 lambda (lambda運算) :
#       運算式(expression)有一個參數(parameter)，
#       運算結果回傳冒號後的運算式。 
#   such as :
f = lambda x: x ** x
print(f(1))