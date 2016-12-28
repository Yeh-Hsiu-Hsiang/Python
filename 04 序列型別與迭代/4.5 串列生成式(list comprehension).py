# P142 串列生成式(list comprehension)
# 語法--> 【運算式 for 名稱 in Iterable】
# 【運算式 for 名稱 in Iterable if 運算式】

ft = [32, 212, 10, 55, 78, 110, 178]
def ftoc(ft):
    ct = []
    for x in ft:
        ct.append((x - 32) * 5 / 9)
    return ct

print(ftoc(ft))
print('---------')

ct = [(x-32) * 5 / 9 for x in ft]
print(ct)
print('---------')

# P143
print([x * 2 for x in range(10)])
print('---------')

li = [32, -77, 53, 12, 90, -3, -6]
li2 = [abs(x) for x in li]
print(li2)
print('---------')

from math import sqrt
scores = [77, 99, 55, 34, 23]
print([int(sqrt(x) * 10) for x in scores])
print('---------')

#       x , y, z
li = [(30, 90, 88), (60, 65, 70), (100, 94, 20)]
print([sum(x) / len(x) for x in li])
print([(x+y+z) / 3 for x, y, z in li])
print('---------')

li = ['a', 'b', 'hi']
print([(x, len(x)) for x in li])
print([[x, len(x)] for x in li])
print('---------')

# P144
li = [('Amy', 10546001, 30, 41, 65),
('Zeo', 10546003, 95, 78, 65)]
print([(x, y, int((z0+z1+z2) / 3)) for x, y, z0, z1, z2 in li])
print('---------')

result = [str(x)+'*'+str(y)+'='+str(x*y) 
for x in range(2, 10)
for y in range(1, 10)]
print(result)
print('---------')

# P145
li = ['a', 'c', 'd']
li2 = ['.jpg', '.png', '.gif']
result = []
for x in li:
    if x != 'a':
        for y in li2:
            if y != '.jpg':
                result.append(x+y)
print('---------')

result = [x+y for x in li if x!='a' for y in li2 if y != '.jpg']
print(result)
print('---------')

li = [[x * 2 for x in range(6)], [x*2 +1 for x in range(6)]]
for x in [y for x in li for y in x if y < 10]:
    print(x)
print('---------')
for x in range(6):
    x *= 2
for x in range(6):
    x *= 2 + 1
for x in y:
    for x in li:
        for y in x :
            if y < 10:
                print(y)