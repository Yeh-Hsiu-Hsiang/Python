# P051 function

# def function_name(參數0, 參數1, ...):    **
# 述句...
# def：保留字 **

# P052
def my_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

scores0 = [60, 73, 81, 95, 34]
scores1 = [10, 20, 30, 40, 50, 60]
total0 = my_sum(scores0)    # call function **
total1 = my_sum(scores1)
print(total0)
print(total1)
print('*------------*')

# P053
def my_len(seq):
    n = 0
    for x in seq:
        n += 1
    return n

seq = my_len('1234567890')
print(seq)
print('*------------*')

# 參數
def ctof(temp):
    n = my_len(temp)
    i = 0
    while i < n:
        temp[i] = temp[i] * 9.0 / 5.0 + 32  # 修改內容
        i += 1

data = [-30.2, -22.5, 15.8, 23.7, 35.2]
ctof(data)  # 把data return function 做處理 **
print(data) # but 無法使用tuple做參數 **
print('*------------*')

def my_sum(numbers, initial):   #兩個參數
    total = initial     # 初始值
    for x in numbers:
        total += x
    return total

scores_minus = [-3, -5, -6, -7, -1, -2]
scores = my_sum(scores_minus, 100)  # 從100開始扣
print(scores)
print('*------------*')


# def my_sum(numbers, initial): ↓↓ **
# def my_sum(numbers, initial = 0): **
# 只傳入一個參數，則initial 預設值為0 **

# P054
scores = [30, 41, 52, 63]
a = my_sum(numbers = scores, initial = 1000)
print(a)

b = my_sum(scores, 1000)
print(b)

print('*------------*')


# return
def total_avg(scores, initial = 0 ):
    n = 0
    total = initial
    for x in scores:
        total += x
        n += 1
    return (total, total / n)

a = total_avg([100, 90, 80, 70, 60])
print(a)
print('*------------*')


# P055
# 存活時間 & 可視範圍(scope) **
a = 3
a += 1
del a
# print(a)
# NameError: name 'a' is not defined
print('*------------*')

a, b = 3, 4
def foo(n):
    m = 5
    return n + m + a
x = foo(b)
print(x)
# y = a + n
# SyntaxError: invalid syntax
print('*------------*')

a = 10
def foo(n):
    a = 100
    return n + a
x = foo(5)
print(x)
print('*------------*')

# P056
a = 10
def foo(n):
    global a    # global 指派到全域 **
    a = 100
    return n + a
x = foo(5)
y = a
print(x, y)
print('*------------*')

# 內建函式
a = [0, 1, 2, 3, 4]
print(len(a))
print(sum(a))
print(sum(a, 1000))
print(max(a),min(a))
print('*------------*')

# P057
range(10) # n-1

li = [30, 41, 52, 63]
range(len(li))
range(5, 12)    # 不含12
range(1, 10, 2) # step 2
range(5, -10, -3)

print('*------------*')

li = [30, 41, 52, 63]
for i in range(len(li)):
    li[i] = li[i] + 100
print(li)
print('*------------*')

print(abs(-3), abs(-4.56))
print(pow(2, 5))
print(pow(333, 0), pow(0, 0))
print(pow(2, 5, 3))     # **後/3取餘數 **
print(round(3.14159, 2))
print('*------------*')

# P058
print(round(1.2345), round(-1.2345))
print(divmod(11, 3))    # 商&餘數 **
print(divmod(11.2, 3))
print('*------------*')

a = ([0, 1], 'hi', True, 3)
b = ([], '', False, 0)
c = ([], '', False, 0, 3)
print(all(a), all(b), all(c))
print(any(a), any(b), any(c))
print('*------------*')

# all 全為True 才return True **
# any 只要一個True就return True **

a, b, c, d, e = 3, 4.56, [0, 1, 2], (30, 41, 42), 'hi'
def f(): pass
print(id(a), id(b), id(c))
print(type(a), type(b))
print(type(c), type(d), type(e))
print(type(f))
print(callable(a), callable(f))
print('*------------*')

# id：物件在記憶體中的位址 **
# class(類別--->可被呼叫) **
# type(型別--->不可被呼叫) **

# P059
print(int(3), int(-4.5), int('678'), int())
print(float(3), float(-4.5), float('67.89'), float())
print(list([0, 1, 2]), list([3, 4, 5]), list('abc'), list())
print(tuple([0, 1, 2]), tuple((3, 4, 5)), tuple('abc'), tuple())
print('*------------*')

a = [0, 1, 2]
b = list(a)     # copy 
print(a == b)
print(a is b)
a[0] = 99
print(a, b)
print('*------------*')

# P060
print(bool(True), bool(False), bool())
print(bool(0), bool(0.0), bool([]), bool(), bool(''))
print(bool(3), bool(4.5), bool([0]), bool((0, )), bool('0'))
print('*------------*')

# bool() 可知某物件True or False **
# repr() 傳入字串 ** 

print(str(3), str(4.5), str([0, 1, 2]), str((3, 4, 5)), str(True), str())
def f(): pass
print(str(f))   # function_Name and memory_address
print('*------------*')

# P061
print(3)
print(3, 4.5, 'hi', [0, 1, 2])
print(3, 'abc', 4.5, sep='/')
print(3, 4, end='xxx')
print(3, 4, end='')
print('*------------*')
# end ='' 寬字串-->不印出新行 **
# end ='xxx' --->預設會印出新行，
# 以關鍵字參數end另行指定 **

a = input()
b = int(a)
print(a, b)
c = input('Your name: ')
print(c)
print('*------------*')