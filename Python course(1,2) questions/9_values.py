tup = (1,2,5,7,4,4)
check = dict()
for i in tup:
    check[i] = check.get(i,0) + 1
for i in tup:
    if check[i]>1:
        print(False)
        exit()
    else:
        continue
print(True)


