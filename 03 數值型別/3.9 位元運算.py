# P102
print(bin(13))
print(int(0b1101))
print('----------')

# P103 二補數
print((2 ** 31) - 1, -(2 ** 31))
# import sys
# print(sys.maxint)
# print(-sys.maxint - 1)
# 2.x版才有
print('----------')

# P104 
print(bin(3))
print(bin(-3))
print('----------')

# 位元運算子
# 運算元只能是整數**
# ~x  Not ex:-(x+1)
# x << y  
# x的每個位元往左位移y次，右手邊新位元填0 
# ex: x*(2**y)
# x >> y
# x的每個位元往右位移y次。 x // (2**y)
# x & y  AND
# x ^ y XOR     x和y不同才為1
# x | y OR

x = 5
print(bin(x))
print(~x)   # Answer 為-6 非-5
print(x << 2)
print(x >> 2)

y = 6
print(bin(y))
print(x & y)
print(x ^ y)
print(x | y)
print('----------')

# P105
x = -10
print(~x)   # Answer 為9 非10
print(x << 2)
print(x >> 2)
y = -5
print(x & y)
print(x ^ y)
print(x | y)
print('----------')

x = 0b10100101
print(x & ~0b111111)
print((x >> 2) & 0b1)   
# 位移後做AND知道該位置位元為0 or 1
print((x >> 3) & 0b1)
print((x & (0b1 << 2)) > 0) # 功能同上
print((x & (0b1 << 3)) > 0)
print(x | (0b1 << 4))
print(x & ~(0b1 << 2))
print(x & ~(0b1 << 2))
print('----------')
# x & 0b1111 四個位元保持原狀其餘為0
# | 可把某些位元設為1，其他位元不變
# x | 0b11110000 --> 4~7位元為1
# 第n個位元，從0開始起跳

def getbits(x, p, n):
    return(x >> (p+1-n)) & ~(~0b0 << n)
# 從第p個位置向右開始拿出位元，共取n個

print(getbits(0b10101010, 4, 3))
print(getbits(0b11110101, 5, 4))

# (x &= y) == (x = x & y)

