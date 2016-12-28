# P133 迭代(iteration)
# 協定(protocol) --> 一套溝通標準。
# 雙方皆遵循才能正常使用。

li = [30, 41, 52]
for x in li:    # for 迴圈迭代串列
    print(x)
# list符合協定提供，for符合協定接收並處理
print('-----------')

itb = iter(li)
print(itb)
print(type(itb))

import collections.abc

print(issubclass(type(itb), collections.abc.Iterator))
print(issubclass(list, collections.abc.Iterable))
# isinstance 實體物件是否符合某型別
# issubclass 型別間繼承關係
print('-----------')

# P135
while True:
    try:
        x = next(itb)
        print(x)
    except StopIteration:
        break
print('-----------')

n = 0 
for i in range(1, 10 + 1):
    n += i
print(n)
print('-----------')

# P136
import collections.abc
a = range(10)
print(a)
print(type(a))
print(issubclass(range, collections.abc.Iterable))
print('-----------')

# 指派
a, b, c = range(3)
print(a, b, c)
a, *b, c = range(10)
print(a, b, c)
print('-----------')

def my_sum(iterable, start = 0):
    result = start
    for x in iterable:
        result += x
    return result

print(my_sum((2, 4, 6, 8), 3))
print(my_sum(['a', 'c', 'f'], 'b'))
print('-----------')

# P137
def product(iterable, start = 1):
    result = start
    for x in iterable:
        result *= x
    return result

def my_factorial(n):
    return product(range(2, n + 1)) # 階乘

print(my_factorial(5))
print('-----------')

def cumulative_sum(iterable, start = 0): 
    result = []
    acc = start
    for x in iterable:
        acc += x    #累和
        result.append(acc)
    return result
def my_cumulative(n):
    return cumulative_sum(range(2, n+1))
print(my_cumulative(7))

# P138
def unique(iterable):   # 挑出唯一的數
    result = []
    for x in iterable:
        if x not in result:
            result.append(x)
    return result

print(unique([3, 5, 7, 9, 3, 8, 8]))
print('-----------')

def duplicate(iterable):    # 挑出重複數值
    fst = []
    snd = []
    for x in iterable:
        if x not in fst:
            fst.append(x)
        elif x not in snd:
            snd.append(x)
        else:
            pass
    return snd
print(duplicate([1, 3, 3, 5, 3, 6, 1, 4, 2]))
print('-----------')

def group(iterable, size):  # 根據size切割list
    result = []
    li = list(iterable)
    length = len(li)
    for i in range(0, length, size):
        result.append(li[i:i+size])
    return result
print(group((1, 3, 5, 7, 9), 2))
print('-----------')

# # P139
def flatten(list2d):    # 壓平二維串列
    result = []         # 二維陣列--> 一維陣列
    for x in list2d:
        result.extend(x)    # append()
    return result
print(flatten(((2, 4), [5, 1, 3], [6], [8, (0, 4)], [0])))
print('-----------')


# 回傳型別enumerate的物件，內容物是tuple
li = ['a', 'b', 'c']
en = enumerate(li)
for i in range(1, 4):
    print(next(en))
print('-----------')

# 同時印出索引值 & 對應元素
li = [90, 80, 75, 61, 72]
for i, v in enumerate(li):
    print(i, v)
print('-----------')
for j in range(len(li)):
    print(j, li[j])
print('-----------')

# 傳入多個迭代，逐一提取元素(tuple)
a = ['a', 'b', 'c']; b = [1, 5, 7]
z = zip(a, b)
for i in range(1, 4):
    print(next(z))
print('-----------')

# P140
li = [90, 89, 80, 56, 73]
li2 =[-10, -0, -5, 2]
result = []
for a, b in zip(li, li2):
    result.append(a+b)
print(result)
print('-----------')

a = [-5, 33, 97, -55, 9]
print(sorted(a))
print(sorted(a, reverse = True))    # 降序
print('-----------')

li = ['Python', 'perl', 'java', 'c', 'ruby']
print(sorted(li))

def keyword(x):
    return len(x)   # 照長度sort
print(sorted(li, key = keyword))

# key 關鍵字參數，必為函數
# 參數為預被排序的元素(自訂排序方法)
print('-----------')

data = [('Amy', 33), ('John', 25), ('Bob', 13)]
print(sorted(data))
def keyword(x):
    return x[1]
print(sorted(data, key = keyword))
print('-----------')

# P141 迴圈原地修改
# numbers = list(range(10))
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         del numbers[i]    # len 變短
#         print(numbers)
# IndexError: list index out of range
# len < 索引值引發錯誤
# print('-----------')

li = [1, 2, 5, 6, 8, 9]
for i, x in enumerate(li):
    print(i, x)
    if x % 2 == 0:
        del li[i]
print(li)     

# i 為索引值，x為元素
# 在途中『更改原先串列』，無法讀取到下個元素