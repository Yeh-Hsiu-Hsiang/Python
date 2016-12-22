# P064 標準程式庫模組
import keyword  # 模組 **
print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.iskeyword('import'))
print(keyword.iskeyword('a'))
print('--------------------')

print(__builtins__) 
print(dir(__builtins__))  
print('--------------------')
# 內建函式dir列出模組內容 **


# P065
import math # 數學函數 **
print(math.pi, math.e)  #常數pi & e
print(math.factorial(6))    # 階乘
print(math.log10(1000), math.log10(99)) # 底數為10之對數
print(math.log(math.e), math.log(1))    #自然對數
print(math.log(32, 2), math.log(1024, 2))   # 底為2之對數
print(math.sqrt(9), math.sqrt(2))
print(math.sin(math.radians(90)))   # 三角函數
print('--------------------')

import random # 隨機亂數(虛擬亂數pseudo random)
random.seed()    # 初始化 **
print(random.random())  # 0~1隨機亂數(浮點)
print(random.randint(1, 7)) # int
print(random.uniform(0.1, 0.5))
li = [2, 99, 132, 44, 0.1]
print(random.choice(li))
random.shuffle(li)   # 弄亂內容 **
print(li)
print(random.choice(range(2, 20, 2)))
print('--------------------')

# P066
import random
random.seed(333)    #輸入某東西做為種子
print(random.random())  # 得到的亂數值相同
print(random.random())
print('--------------------')

# 模組搜尋路徑
import sys
print(sys.path)
print('--------------------')
# ''代表當前目錄


# P067
# 模組之名(__name__)
# 可判斷.py檔被當作主程式檔執行or當作模組匯入

# 匯入未來功能(__future__)
from __future__ import print_function
# 只影響第一個可執行述句程式
# 應該是自創新模組匯入
