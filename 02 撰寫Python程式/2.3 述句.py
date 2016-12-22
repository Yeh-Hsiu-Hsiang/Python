# P038 
# 運算式述句
print(1 + 2)
# print(1 + 2);　# 「;」表示述句結尾 **
print(1 + 2);print(3 + 4);print(5 + 6); 
#  以「;」隔開述句 **
print('*------------*')

a = 3
b = 3 + 5
c = a < b
a = a + 1
#  先運算等號右邊再回傳(指派)給等號左邊 **

a = b = c = 3
b = 4; c = 5
print(a)

x = y = z = [0, 1, 2]
y[0] = 99
z = [30, 41, 52]
print(x, y, z)
print('*------------*')

# P040 序列指派述句
(a, b, c) = (0, 1, 2)
a, b, c = 0, 1, 2
a, b = b, a
print(a,b)
print('*------------*')

x=[0, 1]; i = 0
i, x[i] = 1, 2 #  i先成為1後指派x **
print(x)
print('*------------*')

a, b, c = [0, 1, 2]
[a, b, c] = [0, 1, 2]
a, b, c = 'abc'
print(a, b, c)
print('*------------*')

data = ['John', 165, 52, ('C', 'Python')]
name, height, weight, (lang0, lang1) = data
print(name, height, weight, lang0, lang1)
print('*------------*')

# P041 
# 星號序列指派:用於長度未知情況 **
x = [0, 1, 2, 3, 4]
a, *b, c = x
print(a,b,c)
print('*------------*')

(0, [1, 2, 3], 4)
head, *rest = x
print(head, rest)
print('*------------*')

(0, [1, 2, 3, 4])
*rest, t1, t0 = x
print(rest, t1, t0)
print('*------------*')

([0, 1, 2], 3, 4)
a0, a1, a2, a3, *a4 = x
print(a0, a1, a2, a3, a4)
print('*------------*')

(0, 1, 2, 3, [4])
a0, a1, a2, a3, *a4, a5 = x
print(a0, a1, a2, a3, a4, a5)
print('*------------*')
# 若左邊>右邊則*會顯示[] **
# 剩下數字會放入有*裡  **

# a0, *a1, *a2, a3 =x   # 語法無效

a = b = 3
a += 8
print(a,b)
print('*------------*')

x = y = [0, 1, 2]
x += [98, 99]
print(x,y)
print(x is y)   #   x & y 指向同一物件，故y會隨x變 **
print('*------------*')

x = y = [0, 1, 2]
x = x + [98, 99]
print(x,y)
print(x is y)   #   x & y雖指向同一物件，但只更改x **
print('*------------*')

#   若x += y , x為不可變則 x = x + y  **
#   若x為可變,則修改本身而非產生新物件 **


# P042 
# if 條件判斷述句:程式流程控制(flow control) **

a = 3
#  a = 3    #縮排錯誤，未預期縮排
# IndentationError: unexpected indent

a, b, x = 3, 5, -1
if a < b:
    x = a
    print(x)
print('*------------*')

t = 999; x = None
if t < 0:
    x = -1
elif 0 <= t and t <= 100:
    x = t
else:
    x = 101
print(x)
print('*------------*')
# 無法單獨elif or else , 必須搭配if使用 **


# P044
a, b, c = 3, 5, 7; x =None
if a < b:
    if b < c:
        x = c
    else:
        x = b
else:
    if a < c:
        x = c
    else:
        x = a
print(x)
print('*------------*')

# if a < b --> SyntaxError: invalid syntax 


# P045
a, b, c = 0, '', []
if a and b and c: # false
    print('hi')

# pass 述句
a, b = 3, 5
if a < b:
    print('a < b')
else:
    pass
print('*------------*')


# P046
# while迴圈述句

i = 1
x = 0
while i <= 100:     
    x += i
    i += 1 
print(x,i)
print('*------------*')    
# while ~ :稱之為「頭」 **
# 條件符合才執行 **
# 程式形式為「重複執行」　or　「迭代(iteration)」 **

# P047
scores = [60, 73, 81, 95, 34]
n = 5
i = 0
total = 0
while i < 5:
    total += scores[i]
    i += 1
avg = total / n     # avg = average
print(avg)
print('*------------*')  


# for迴圈述句
scores = [60, 73, 81, 95, 34]
n = 0 
total = 0
for x in scores:
    n += 1      #len
    total += x 
avg = total / n
print(avg)
print('*------------*') 

# for Name in 一連串物件(list) **
# 將單一物件指派給Name **


# P048
s = 'Hello Python'
e_count = 0
for x in s:
    if x =='e':
        e_count += 1
print(e_count)
print('*------------*') 

names_scores = (('Amy', 82, 90), ('John', 33, 64), ('Zoe', 91, 94))
highs = []
for x, y, z in names_scores:
    if y >= 90 and z >= 90:
        highs += [x, y, z]
print(highs)
print('*------------*') 

# P049 雙重迴圈
colors = ['red', 'green', 'blue']
animals = ['cat', 'dog', 'horse', 'sheep']
results = []
for x in colors:
    for y in animals:
        results += [x + ' ' + y]
print(results)
print('*------------*') 

# break   
scores = (98, 78, 64, 55, 61, 82)
lower_than_60 = False
for x in scores:
    if x < 60:
        lower_than_60 = True
        break   # 跳出迴圈
print(x)
print('*------------*') 

data = [[33, 44, 55], [18381, 99781], [60, 70, 42, 91], [32, 51]]
total = 0
for x in data:
    for y in x :
        if 0 <= y <= 100:   # data正確
            print(y)
            total += y
        else:
            break
print(total)
print('*------------*') 

# continue
scores = [60, 73, 81, 95, 34]
n = 0
high_total = 0
for x in scores:
    if x < 60:
        continue    # 跳到下輪
    n += 1
    high_total += x
print(n)
print(high_total)
print('*------------*') 

scores = [30, 99, 41, 55, 84]
scores_new = []
for x in scores:
    if x >= 90:
        scores_new += [x]
        continue
    x += 10

    if x >= 90:    # 加分上限
        x = 90
    scores_new += [x]

print(scores_new)
print('*------------*')

# break 直接離開最近之迴圈 **
# continue 跳到下一輪迴圈 **
# exit() 直接離開程式 **

# assert：斷言述句，用於除錯 **
# pass 
# del：刪除名稱 & 物件綁定關係 **
# print 
# return：exit function and return Value or None 
# yield：用於產生器函式內 **
# raise：引發異常 **
# break：use for & while
# continue
# import：匯入模組 **
# global：全域範圍宣告 **
# nonlocal：外圍函式範圍宣告 **
# if
# while & for
# try：異常處理 **
# with：把一組程式述句包起來，由文脈管理器負責進入&離開的情況 **
# def：function
# class：類別定義 **



