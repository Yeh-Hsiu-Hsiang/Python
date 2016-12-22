i, j = 1, 1
while i <= 9:
    while j <= 9:
        total = i * j
        print(str(i) + '*' + str(j) + '=' + str(total))
        j += 1    
    i += 1
