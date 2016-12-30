# P145 string
# Python 沒有字元(character)
# 含有一個字元的string
# 不可變type

print('')
print('hello')
s = 'hi'
print(type(s))
print(s)
ss = 'abc def \
ghi jk \
lmnop'
print(ss)

# \換行(不間斷)**
# \挑脫字元(跳脫碼)
#-----------------------------------#
#   跳脫串   |         意義         |
#------------|----------------------|
#     \'     |      單引號「'」     |
#     \"     |      雙引號「"」     |
#     \\     |      反斜線「\」     |
#     \n     |     插入一行(換行)   | *ASCII 的LF
#     \r     |       游標返回       | *ASCII 的CR
#     \t     |       水平定位       | *ASCII 的TAB
#     \v     |       垂直定位       | *ASCII 的VT
#     \a     |         鈴響         | *ASCII 的BEL
#     \b     |       退後一格       | *ASCII 的BS
#     \f     |       插入一頁       | *ASCII 的FF
#    \xff    |   以十六進位表示字元 |
#    \ooo    |    以八進位表示字元  |
#-----------------------------------#

print('------------------')
# P147
print('What\'s your name?')
print('abc\"de\'fg')
print('ab\c\d')
print('ab\c\n\d')
print('abc\ndefg')
print('\x66')
print('\155')
print('------------------')

# P148
s = '''abc def
ghi jkl     mno
vw'''
print(s)
print('''abc\'\'\'def''')
print('------------------')

# 三重引號間換行引號無須跳脫

#開頭引號前加上R or r代表(raw)原始
print('\n')
print(r'\n')
print('------------------')

# P149
# ord 查字元的ASCII碼(傳入參數只能len為1的string)

print(ord('a'))
print(ord('\n'), hex(ord('\n')))
print('------------------')

# P152
# islower() --> 字串中只要有字母並為小寫回傳true
print('a123$%^&'.islower())
print('------------------')

# P153
# 空白字元 --> ''、'\t'(TAB)、'\v'(VT)、'\n'(LF)
# '\r'(CR)、'\f'(FF)

print('\t\v\n\r\f'.isspace())
print('------------------')

print('asd fgh hjkl'.find('asd')) 
# return index from index(1)
print('asd fgh hjkl fgh ew'.find('fgh', 4, 7))
# 反向find, start, end
print('asd fgh hjkl'.find('zxc'))
# not find return -1
print('asd fgh hjkl fgh ew'.replace('fgh', '123', 1))
# 只換掉前一個
print('------------------')

# strip() 去除空白字元
# lstrip() 去除首端
# rstrip() 去除尾端
# ljust() 字串靠左
# rjust() 字串靠右
# zfill() 補0
# expandtabs() TAB換成空格字元 ()-->指定欄寬度
print(' Hello Python \t\n '.lstrip('\n\t Hn'))
print(' Hello Python \t\n '.rstrip('\n\t Hn'))
print('------------------')

# P156
li = ['Hello', 'Python', 'hi']
print(' '.join(li))
print('*'.join(li))
print('------------------')
# 以''作為分隔符

# splitlines 分割成行
print('Hello\nPython'.splitlines())
print('------------------')

# P157  字串格式化%
print('Hello %i Python' %2)
print('I\'m %i years old. My cat\'s name is %s' %(20, 'yellow'))
print('------------------')

# P159
print('%X %#X' % (999, 999))    # 十六進位
print('%o %#o' % (10, 10))  # 八進位
print('%8i %8i' % (123, 456))  # 占8個字元寬度
print('%08i %08i' % (123, 456)) # 填補0
print('%-8i %8i' %(123, 456))  #靠左對齊
print('%f %.2f' %(1.234, 2.3456))   # 指定小數位數
print('------------------')

# P160
# def p99(li):
#     for y in range(1, 10):
#         result = []
#         for x in li:
#             s = '%2i x%2i = %2i' %(x, y, x*y)
#             result.append(s)
#     print('    '.join(result))
# print(p99([1, 2, 3, 4, 5]))
# print('')
# print(p99([6, 7, 8, 9]))

# P161 字串格式化format
print('{2} {1} {0}'.format(123, 45.67, 'hi'))
test = '{} {} {}'
print(test.format('hi', 'Python', 'good morning'))
print('{{}}'.format())
print('------------------')

# P163
# fill：任何填補字元，除大括號外。
# align：「<^>」靠左中右對齊，「=」填補
# sign：「+」「-」空格，同「%」格式指定子
# #：同「%」格式指定子
# 0：同「%」格式指定子
# width：欄寬，同「%」格式指定子
# ,：每千加上,。
# .precision：精確度，同「%」格式指定子
# typecode：同「%」格式指定子(幾乎)
# b代表二進位，s參數必為string

print('{:d}, {:#X} {:#b}'.format(200,200,200))
print('{:-08}, {:+8}'.format(3.14, 12.567))
print('{:<-08}, {:>+8}, {:^8}'.format(3.14, 12.567, 76))
print('{:,}, {:,}'.format(1234567809, 9804.2341))
print('{0:>{2}.2e}, {1:>{2}.2e}'.format(3.14, 12.67, 10))
# 參數指定欄寬
print('------------------')


# P165 漢明距離(hamming distance)
# 又稱為信號距離，兩字串間不同字元個數
def hamming(s1, s2):
	lens = (len(s1), len(s2))
	minlen = min(lens)
	maxlen = max(lens)
	h = maxlen - minlen
	
	for i in range(minlen):
		if(s1[i] != s2[i]):
			h += 1
	return h
print(hamming('qwerty', 'ytrewq'))
print('------------------')

# 重組字(anagram)↓↓
# 把字串字元重新排列組合，成新詞彙。
def is_anagram(s1, s2):
	s1 = ''.join(s1.lower().split())
	s2 = ''.join(s2.lower().split())
	return sorted(s1) == sorted(s2)
print(is_anagram('arm', 'mra'))
print('------------------')

# P166
alphabet = 'ABCDEFGH0987654321POIUYTR'
def base36encode(number, alphabet=alphabet):
	result = []
	base = len(alphabet)
	sign = ' '
	if number < 0:
		sign = '-'
		number = -number

	while number >= base:	# 大於36進位
		number, i = divmod(number, base)	
		# 除36取商&餘數
		result.append(alphabet[i])
		# 找出對應字元並append
	result.append(alphabet[number])

	if sign == '-':
		result.append(sign)

	return ''.join(reversed(result))  # 逆轉
print(base36encode(-9, alphabet))