d = {}  # 建立空字典物件
d = {'name': 'Amy', 'age':27}   # 以大括號語法建立dict(字典)物件
print(d)
print(d['name'])
d['age'] = 29
print(d['age'])
# print(d['score'])     # KeyError: 'score'

# 字典不具順序性
# 字典不限於整數
# ex:鍵(key):name，值(value):Amy
# 鍵為不可變物件
# 可從任意地方開始起跳
# (不像list要從index[0]開始)

print('-------------------')

# P176
d = dict(name='Amy', age = 40, job ='writer')
keys = ['name', 'age', 'job']   # 含有鍵的list
values = ['Amy', 40, 'writer']  # 含有值的list

d2 = dict(zip(keys, values))    # 內建函式zip組合
print(d2)

d3 = dict(d2, name='Amanda')
print(d3)

d4 = dict(zip(range(100, 100 +3), ('Amy', 'Bob', 'Cathy')))
print(d4)
print('-------------------')

d = {'name' : 'Tina', 'age': 20, 'score': 77}
del d['name']
print(d.get('name', 'Amy'))   # 以方法get取用，若無該鍵則return 預設值'Amy'
d.setdefault('job')   # 以方法setdefault指派，預設值(無該鍵)
print(d)

print('age' in d)
print(20 in d)
#  只能判斷鍵無法判斷值
print('-------------------')

# set(集合)：傳入含有元素(一個個)，傳入值必為不可變物件
# remove：若不存在會出錯
# discard(移除元素)：不存在不出錯
# & 交集(intersection)
# | 聯集(union)
# - 差集(difference) (前)
# ^ 對稱差集(symmetric difference) (前後)

