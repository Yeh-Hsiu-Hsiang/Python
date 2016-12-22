# P076
print(False - 5 + (True * 3))
print(True == 1, False == 0)
print(True is 1, False is 0)
print('--------------------')

x, y, z = 3, 6, 9
print(x < y and y < z)
print(x < y < z)
print(x < y and y > z)
print(x < y > z)
print(x == y < z)
print(x == y and y < z)
print('--------------------')


print((0, 1, 2, 3))
print(3 * (4 + 5))
print((0))
print((0, ))
print('--------------------')

# P077
# 迴圈述句的else子句
numbers = [1, 5, 13, 7, 2, 9]
hasEven = False
for x in numbers:
    if x % 2 == 0:
        hasEven = True
        break
else:
    hasEven = False
    