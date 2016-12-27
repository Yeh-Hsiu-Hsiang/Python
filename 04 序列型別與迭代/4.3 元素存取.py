# P122 元素存取
# 序列型別是種容器，內容物稱為元素

# 索引
li = [30, 41, 52, 63, 74, 85]
print(li[0])
print(li[5], li[len(li) -1])
# print(li[99])
# IndexError: list index out of range
s = 'hello python'
print(s[0], s[6])
print(s[0], s[6], s[len(s) -1])
print('-------------------')

# s[-i] =s[len(s) -i]
# -1(最後的元素)


# P123
li = [30, 41, 52, 63, 74, 85]
print(li[-1], li[len(li) - 1])
print(li[-2], li[-5], li[-6], li[-len(li)])
print(li[0], li[-0])
# print(li[-7])
# IndexError: list index out of range
print('-------------------')

li = [30, 41, 52, 63, 74, 85]
li [0] = 'Amy'
li[len(li) - 1] = ('a', 'b', 'c')
print(li)
print('')

li2 = ['a', 'b', 'c']
li[-1] = li2
print(li)
print('')

li2[0] = 'abc'
print(li)
print(li[-1] is li2)
print('-------------------')

li = [30, 41, 52, 63, 74, 85]
del li[0]
print(li)
del li[-1]
print(li)
print('-------------------')

# P124  切片(slicing)
# i為起始索引值，j為結束索引值(不包含)
li = [30, 41, 52, 63, 74, 85]
print(li[0:3])
print(li[2:])
print(li[:4])
print(li[5:3])
print(li[99:3])
print(li[3:99]) # 99被視為長度
print(li[:])
first, rest = li[0], li[1:]
print(first, rest)
first, *rest = li   # 星號序列指派，拿出第0個與其他
print(first)
print(*rest)
print('-------------------')

li = [30, 41, 52, 63, 74, 85]
print(li[-4:-2])
print(li[-2:])
print(li[:-3])
rest, last = li[:-1], li[-1]
print(rest, last)
*rest, last = li
print(*rest)
print(last)
# *集中其他元素
# s[i:j:k] --> k不可為0 **
print('-------------------')


# P125
li = [30, 41, 52, 63, 74, 85]
print(li[1:5:2])
print(li[-1:1:-2])
print(li[::-1]) # 逆轉
print(li[-1:1]) # 不會逆轉，被視為len
print(li[::-2])
a, b, c = li[1:4]
print(a, b, c)
a, *b = li[1::2]
print(a)
print(b)
print('-------------------')
# 若為:開頭，則從尾開始跑**

li = [30, 41, 52, 63, 74, 85]
li[0:2] = 'a', 'b'  # 不包含li[2]
print(li)
li[1:3] = 'x', 'y', 'z' # 不包含li[3]
print(li)
# li[0:2] = 9999
# TypeError: can only assign an iterable
# 必為可迭代

li[0:2] = []
print(li)
li[1:-1] = []
print(li)
print('-------------------')

del li[0]
print(li)
li = [30, 41, 52, 63, 74, 85]
del li[-3:-1]
print(li)
del li[:]   # del所有元素
print(li)
# del li      # del 名稱li，解除與物件綁定
# print(li)
# NameError: name 'li' is not defined
print('-------------------')

# 比較
li = [3, 4, 5, 7]
li2 = li[:]
print(li == li2, li is li2)
li2.append('hello')
li.append('ha')
print('ha' in li, 'ha' in li2)
print('hello' not in li, 'hello' not in li2)
print(('ha', 5) in li, ('ha', 5)in li2)
# ('ha', 5) is a tuple，false
print(['hello', 7] in li2, ['hello', 7] in li)
print('-------------------')

li = [['a', 'b'], ('x', 9, (3, 4)), 5, 6]
print(('x') in li, ('x') not in li)
print(['a', 'b'] in li, ['a', 'b'] not in li)
print((3, 4) in li, (3, 4) not in li)
print(('x', 9, (3, 4)) in li, ('x', 9, (3, 4)) not in li)
# ('x', 9, (3, 4)) 為一物件，不可分
print('-------------------')

#運算子
li = [0, 1, 2]; t =(3, 4, 5); s = 'Hello'
print(li + [30, 40, 50])
print(t + ('a', 'b', 'c'))
print(s + 'Python')
# print(li + t + s)
# TypeError: can only concatenate list (not "tuple") to list
# 不能連接type tuple

print(li + list(t)) # 轉換型別
print(tuple(li) + t)
print('-------------------')

# P128
# 原地修改(extend) -->用於type tuple
# type str ---> join()
# type bytes ---> join() or bytearray(可變型別)
# *代表copy，淺複製(shallow copy)
# 淺複製 --> 複製物件(含位置)，別名現象
# 新物件會指向同一物件(改新物件原物件也會跟著改變) **
# 深複製 --> 複製物件(新建) **

li = [[0, 1, 5], 8]
li2 = li * 3
li3 = li.copy()
print(li2)
li[0][0]= 9     
li[1] = 0
print(li)
print(li2)
print(li3)
print('-------------------')

li = [[0, 52, 63, 75], [88, 99]]
li[0] = 99
li2 = li * 3
li3 = li.copy()
li[1][0] = 66
print(li)
print(li2)
print(li3)
# 先copy再更改，li2不變(list)
# 雙list 則會一起更改
print('-------------------')

# P129  內建函式
print(slice)
li = [0, 1, 2, 3, 5, 7]
s0 = slice(0, 2); s1 = slice(1, 7, 2)
print(li[s0], li[s1])
print(s1.start, s1.stop, s1.step)   # 方法
data = '2016/12/27 08:00 T:26.5C H:50% P:1013hPa'
ST = slice(19, 19+4)    #溫度
SH = slice(27, 27+2)    #濕度
SP = slice(33, 33+4)    #氣壓
# 先做切片slice
print(data[ST], data[SH], data[SP])
print('-------------------')

# P130
print(range)
print(range(100))
print(list(range(1,50)))
print('-------------------')

a = [9, 8, 3, 5, 7]
r = reversed(a)
print(r)    # r為迭代器**
print(next(r))
print(sorted(a))
# reversed 逆向一次傳回一個元素(list)**
print('-------------------')

a = [0, 3, 7, 1]; b = ['z', 'x', 'y']
print(zip(a, b))
print(list(zip(a, b)))
x = enumerate(b)
print(next(x))
print(next(x))
y = enumerate(a, 50)    # 指定起始值**
print(next(y))
print(next(y))
print(next(y))
# enumerate 回傳迭代器(tuple)**
print('-------------------')


# P131 方法
li = [2, 5, 4, 'a', 'y', [1, 0], (5, 7), 3]
print(li.index(5))  # 找出()內索引值
print(li.index('y', 2))   # 指定起始尋找位置
print(li.index(3, 3, len(li)))  #指定結尾索引值
print(li.count('a'))    # 出現次數

# li.pop()拿出最後一個並刪除
# li.copy() 淺複製
print('-------------------')


li = [0, [1, 2], 3]
li2 = li[:]; li3 = li.copy(); li4 = list(li)
import copy
li5 = copy.copy(li)
li6 = copy.deepcopy(li)
li[1][1] = 999
print(li == li2 == li3 == li4 == li5)
print(li == li6, li != li6)
print(li is li2, li is li6)
# li~li5內容相同但為不同物件
# li6 內容看起來雖相同但不指向同一個地方