# P083 int & float
print(type(3), type(3.0))
print(1.0 / 3.0)
print(0.1)
n = 0.1 + 0.2
print(n)
print(n == 0.3, abs(n - 0.3) < 0.001)
sum = 0
for i in range(10):
    sum += 0.1
print(sum)
print('-------------------')

# 十進位(decimal)
# 二進位(binary)
# 十六進位(hexadecimal)
# 八進位(octal)

# P084
print(0b1100100, 0x64, 0o144)
print(0B1100100, 0X64, 0O144)
print('-------------------')

# bin()、hex()、oct() 把int-->str
print(bin(100), hex(100), oct(100))
print(bin(255), hex(255), oct(255))
print('-------------------')

print(0b10000, 0x10, 0o20)
print(int(0b10000), int(0x10), int(0o20))
print(int('99', 10), int('99'))
print(int('0b11', 2), int('11', 2))
print(int('0xFF', 16), int('FF', 16))
print('-------------------')

# P085
print(int('0o77', 8), int('77', 8))
print(int('0b11', 0), int('0xFF', 0), int('0o77', 0))
print(int('12AFGZ', 36))
print(int(3.14))
print('-------------------')

print(3.0, 1., 456.789)
print(3e8)  # 光速(公尺/秒)
print(45E6)
print(6.02e23)  # 莫耳(mole)
print(1e-6) # 微米(1米的百萬分之一)
print('-------------------')

print(float())
print(float(-3), float(0xFF))
print(float(3.14), float(-4.5e6))
print(float('3.14'), float('-4.5e6'))
print('-------------------')

# float('nan') --> 非數字(Not a Number)
# float('inf') --> 正無限大
# float('-inf') --> 負無限大

# P086
print(float('nan'), float('inf'), float('-inf'))
print('Infinity', float('-infinity'))
print(1e400, -1e400)
nan = float('nan'); inf = float('inf')
print(inf == inf, nan == nan)
import math
print(math.isnan(float('nan')))
print(math.isinf(float('inf')))
print(math.isfinite(float('inf')), math.isfinite(float('nan')))
# 除了inf & nan之外的數字才return True
print('-------------------')

# abs() --> 絕對值
# divmod() --> 商 & 餘數
# pow() --> 冪次方
# round() --> 四捨五入
print(round(3.144, 2), round(3.145, 2))
print(round(1.2), round(-1.2))
print(round(2.675, 2))
print('-------------------')

# P087
a = 1e400
print(a)
print(a / 99999, a * -7, 3 / a)
print(a / a, float('inf') / float('-inf'))
import math
print(math.sqrt(float('nan') + 23 / 2 * 555))
print('-------------------')

print(1 / 3 , 1.0 / 3)
import math
print(17.0 // 3, math.floor(17.0 / 3), math.trunc(17.0 / 3))
# // 地板除法(小於等於某數), 截斷(trunc)
print(-17.0 // 3, math.floor(-17.0 / 3), math.trunc(-17.0 / 3))
print('-------------------')

# P088
print(math.sqrt(9), math.sqrt(10))
print(math.pow(27, 1.0 / 3), math.pow(125, 1.0 / 3))
print(math.pow(16, 1.0 / 4), math.pow(81, 1.0 / 4))
