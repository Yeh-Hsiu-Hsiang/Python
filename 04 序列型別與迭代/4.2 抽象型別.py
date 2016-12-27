# P117 抽象型別
# 序列(Sequence)為抽象型別(不能產出物件)
# list、tuple、str為實際型別(可產出物件)
# 可變序列(MutableSequence)
# isinstance 得知物件是否符合某型別(&抽象型別)
# issubclass 可知型別間的繼承關係(含抽象型別)


# P119
from collections.abc import *
li = [0, 1, 2]
t = (3, 4)
print(len(li), len(t))
print(0 in li, 1 in t)
print(li[0], t[1])
li.append(99); # t.append(99)	
# AttributeError:
# 'tuple' object has no attribute 'append'
print(isinstance(li, list), isinstance(t, tuple))	
# li符合list型別，t符合tuple
print(isinstance(li, Sequence), isinstance(t, Sequence))	# 皆為序列
print(isinstance(li, MutableSequence), isinstance(t, MutableSequence))
print(issubclass(list, Sequence), issubclass(Sequence, Sized))	
# list 繼承Sequence，又繼承Sized
print(issubclass(MutableSequence, Sequence))
# MutableSequence 繼承自Sequence
print(issubclass(tuple, Sequence), issubclass(tuple, MutableSequence))
print('-----------------------------')

# P120
# 可迭代者(lterable) & 迭代器(lterator)
# 抽象型別定義lterable，lterable定義「逐步取出下個元素」
# type list符合lterable，so list可建立出lterable物件
# 拿到lterable物件便可逐一取出list內元素

li = [30, 41, 52]
lit = iter(li)
print(lit)
print(next(lit))
print(next(lit))
print(next(lit))
print(next(lit))	# 沒下一個，StopIteration
print('-----------------------------')

# P121
# 序列型別操作動作 & 結果
# x in s 、 x not in s
# s is t 、s is not t  --> 測試是否為同一物件
# s + t
# s * n、n * s   --> s copy n次 then connect
# s[i]	--> s第i個元素(起始值為0)
# s[i:j]	--> 從第i個到第j個(不含)
# s[i:j:k]	--> 		′′			，每次跳k個
# len(s)
# min(s)
# max(s)
# s.index(x)、s.index(x[, i[, j]])	--> s裡x第一次出現的索引值，i、j指定搜尋界限
# s.count(x)

#-----------------------------#

# 可變序列型別操作動作 & 結果
# s[i] = x 		-->  s的第i個置換為x
# del s[i]		--> 刪除s裡第i個元素
# s[i:j] = t    --> i~j(不含)置換為t
# del s[i:j]	--> == s[i:j] = []
# s[i:j:k] = t  --> i，j，k置換為t
# del s[i:j:k]	
# s.append(x)	--> == s[len(s):len(s)] = [x]
# s.extend(t)	-->	== s[len(s):len(s)] = t (附加t的內容物到末端)
# s.clear()		--> == del s[:]
# s.copy()		--> == s[:]
# s.insert(i, x) --> x插入i的位置， == s[i:i] = [x]
# s.pop([i]) 	--> 拿出並移除索引值為i的元素
# s.remove(x)	--> == del s[s.index(x)](刪除s裡的x)
# s.reverse()	--> 逆轉s裡元素
