# P088
a = list(range(1, 100 + 1 ))
print(sum(a), len(a))
print(sum(a) / len(a))
print(float(sum(a)) / len(a))
print('----------------')

def geomean(numbers):
    product = 1
    for n in numbers:
        product *= n
        return product ** (1.0 / len(numbers))
print('----------------')

# P089
diff = 0.00001
def is_ok(n, ans):
    return abs(ans ** 2 - n) < diff
def get_better(n, ans):
    return ((float(n) / ans) + ans) / 2
def my_sqrt(n):
    ans = 1
    while not is_ok(n, ans):
        ans = get_better(n, ans)
        return ans
print(is_ok(1, 2))
print(get_better(1, 2))
print(my_sqrt(2))
print('----------------')
# 牛頓法--> 求n的平方根時
# 假設 ans = 1
# 判斷後若答案不好 把(n / ans + ans) / 2 作為答案(更接近)
# 重複直到ans的平方 & n相差介於一定程度內


