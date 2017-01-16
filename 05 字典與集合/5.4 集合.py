# P192  建立集合
empty_dict = {}     # 建立空字典
empty_set = set()   # 建立空集合


# P195  集合生成式
# { 運算式 for 名稱 in Iterable}
# { 運算式 for 名稱 in Iterable if 運算式}

# example:
li = ['a', 'bar', 'candy', 'o', 'car']
print({x for x in li if len(x) == 1})
print('---------')
for x in li:
    if len(x) == 1:
        print(x)
print('-------------------------')


# P196  埃氏篩法(找質數)
def prime_sieve(n):
    primes = set(range(2, n+1))

    for i in range(2, (n+1+1) // 2):
        if i in primes:
            m = 2
            while i * m <= n:
                primes.discard(i * m)
                m += 1
    return primes

print(prime_sieve(10))