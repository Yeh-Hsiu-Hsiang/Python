pi = 3.14

def gcd(a, b):  # 求最大公因數
    while b:
        a, b = b, a % b
        return a

def factorial(n):   # 階乘
    result = 1
    for i in range(1, n+1):
        result *= i
        return result

if __name__ == '__main__':  #被import匯入為檔名
	print('as main program')
else:
	print('as module')
	