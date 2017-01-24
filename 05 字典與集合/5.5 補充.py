# P196
# defaultdict -->可先給定預設值
# 當key不存在dict內時，自動建立

from collections import defaultdict


print(int())

d = defaultdict(int)
print(d['a'])

d['c'] = 3
print(d)

s = 'banana'
for x in s:
    d[x] += 1
print(d)

print('-----------')

# P197
# 順序性dict

from collections import OrderedDict


d = OrderedDict()
d['a'] = 2
d['b'] = 4
d['c'] = 6
print(d)

del d['a']
d['a'] = 2
print(d)
print('-----------')


# popitem --> True :尾端提取 & del
#         --> False : 首端提取 & del

d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)
print(d.popitem())
print(d.popitem(False))
print(d)
print('-----------')

d = OrderedDict([('a', 1), ('b', 2), c=3, ])
