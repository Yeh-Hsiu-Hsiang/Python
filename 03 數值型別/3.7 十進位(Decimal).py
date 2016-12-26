# P097
from decimal import *
print(Decimal)
print(Decimal(0.1))
print(Decimal(3.14))
print(Decimal('0.1'), Decimal('3.14'))
D = Decimal
print(Decimal('0.1') * 3 - Decimal('0.3'))
print('------------------------------')

# P098
a = D('0.20'); b = D('0.40')
print(a + b)
print(a * b)
print('---------------------------')

a = D('1.23'); b = D('4.56'); c = D('7.89')
li = [a, b, c]
print(max(li), min(li), sum(li))
print(int(a), float(a))
print(a.sqrt())
print(b.exp())
print(c.log10())
print(a.sqrt().quantize(D('0.01'), ROUND_CEILING))
print(b.exp().quantize(D('0.001'), ROUND_HALF_UP))
print('---------------------------')

# 算術環境：記錄各種設定**
# user設定精確度(預設28位數)、
# 捨入規則、指數限制..等。


# P099
print(getcontext()) # 取得算術環境**
print(getcontext().prec)    # 預設位數**
print(Decimal(1) / Decimal(7))
getcontext().prec = 4   # 更改位數**
print(Decimal(1) / Decimal(7))
print(getcontext().rounding)   # 預設捨入規則
print(D('1.2341') + D('0.0005'))
print(D('1.2341') + D('0.0004'))
getcontext().rounding = ROUND_UP
print(D('1.2341') + D('0.0001'))
print('---------------------------')

# 捨入規則：
# ROUND_CEILING --> 朝著無限大的方向
# ROUND_DOWN --> 朝著接近0的方向
# ROUND_FLOOR --> 朝著負無限大
# ROUND_HALF_DOWN --> 四捨六入，五朝著0
# ROUND_HALF_EVEN --> 四捨六入，五朝最靠近偶數
# ROUND_HALF_UP --> 四捨六入，五遠離0
# ROUND_UP --> 遠離0
# ROUND_05UP ↓↓
# 若最後位數朝著0方向捨入後為0 or 5 -->遠離0
# else 朝著0

# 十進位數算術規格(General Decimal Arithmetic)
# 信號(signal)：若計算中發生狀況
# (除以0, 捨入導致結果不確實, 溢位)
# 可觀察相關旗標，中途攔截著手處理。
