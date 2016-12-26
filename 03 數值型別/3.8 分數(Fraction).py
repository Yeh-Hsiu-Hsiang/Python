# P100 
# 分數(Fraction) 為不可變物件 **

from fractions import *
print(Fraction)
print(Fraction(1, 3))
print(Fraction(16, -10))
F = Fraction
print(F('-1/3'))
print(Fraction('1.414'))
print(F(F(1, 3), F(2, 10)))
# print(F(1.1, 2))
# TypeError: 
# both arguments should be Rational instances
# print(F(1.1))
# 只傳入一個浮點數，but ↓↓
# 2476979795053773/2251799813685248
import decimal
print(F(decimal.Decimal('1.1')))
print(F())  # 無參數為0
print('---------------------------')

# P101
a, b, c = F('1/3'), F('17/3'), F('5/12')
print(a + b, b - c, c * a, a / b)
print(abs(a-b), round(b))   # abs絕對值
print(gcd(64, 48))  # gcd最大公因
print('---------------------------')

a = F('3.1415926535897932')
print(a)
print(a.limit_denominator())    # 預設限定6位
print(a.limit_denominator(100)) # 預設限定2位
print(F(1.0 / 3).limit_denominator())
# 無窮小數近似分數