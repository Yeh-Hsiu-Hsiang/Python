# P185  字典
# d.get --> 回傳鍵的對應值
# d.popitem() --> 取出鍵值並刪除

# P186  建立字典
from decimal import Decimal
from fractions import Fraction
d = {1: 111, 'a': 2, Decimal('3.14'): 'pi', Fraction(1, 3): 1.3}
print(d)
print(hash(1.0), hash(1))   # key(鍵)
print(d[1.0], d[1])
print('-------------------------')


# print(dict(foo = 1, bar = 2, 123abc = 3))
# SyntaxError: invalid syntax


# P187  字典生成式(dict comprehension)
# { 運算式: 運算式 or 名稱 in Iterable}
# { 運算式: 運算式 for 名稱 in Iterable if 運算式}

# example:
print({k: k ** 2 for k in range(5)})
print(dict([(k, k**2) for k in range(5)]))

d = {'Amy': 90, 'Joe': 45, 'Kevin': 33}
print({k: v for k, v in d.items() if v < 60})

li = ['a', 'b', 'c']
print({a: i for i, a in enumerate(li, start=101)})
print('-------------------------')


# P188
# enumerate 列舉
# enumerate 组成索引序列，可取得值 & 索引

print(dict(enumerate(li, start = 101)))
print('-------------------------')
