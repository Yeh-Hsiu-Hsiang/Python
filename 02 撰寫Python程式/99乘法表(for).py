total = 1
for i in range(1,10):
    for j in range(1,10):
        total = i * j
        print(str(i) + '*' + str(j) + '=' + str(total))
        j += 1
    i += 1
