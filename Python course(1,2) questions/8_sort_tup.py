tup = (('x',45),('y',12),('z',20))
temp = list()
for k,v in tup:
    temp.append((v,k))
temp = sorted(temp)
tup2 = list()
for v,k in temp:
    tup2.append((k,v))
print(tup2)

