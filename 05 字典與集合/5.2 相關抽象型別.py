# P179  Hashable(可雜湊者)
# 類似於list，index(0) = values('string')
# 若物件為容器，則內容物&物件容器必須皆為不可變

print(hash('a'), hash('abc'), hash((30, 41, 52)))

a = 2; b ='asdf'; c = (10, 30, 50)
print(hash(a), hash(b), hash(c))
print(hash('name'))
print('--------------------')

# P181  Mapping(映射)

d = {'name': 'Amy', 'age': 20, 'score': 77}
d.pop('name')   # 移除配對
print(d)
d.update({'name': 'John', 'age': 33, 'job':'wrier', 'score': 80})   # 更新內容
print(d)