import mymath   # 匯入模組(不用副檔名)

print('---Hello Python---')
print('pi is ' + str(mymath.pi))
print('gcd of 24 and 16 is ' + str(mymath.gcd(24, 16)))
print('factorial of 6 is ' + str(mymath.factorial(6)))
print('---Bye Python---')

# 模組具有命名空間(namespace)功能 ↓↓
# 可存放東西(名稱)
# 匯入-->以模組名稱存取模組內物件
# 模組檔名會成為識別字(不可.-空格)

print('***********************')

from mymath import * # 把mymath 匯入到全域
print('pi is: ' + str(pi))
print('gcd of 12 and 60 is ' + str(gcd(12, 60)))
print('factorial of 6 is ' + str(factorial(6)))
print('***********************')

from mymath import pi, gcd, factorial
print(pi)
print(gcd(12, 60))
print(factorial(6))
print('***********************')

import mymath as m # m取代mymath名稱較簡潔呼叫
print(m.pi)
print(m.gcd(12, 60))
print(m.factorial(6))
print('***********************')

if __name__ == '__main__':	#主程式name為字串
	print('as main program')
else:
	print('as module')