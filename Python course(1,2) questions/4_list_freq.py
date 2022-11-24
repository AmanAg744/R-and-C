list = [1,3,2,2,1,2,3,0,0]
freq = dict()
for i in list:
    freq[i]  = freq.get(i,0) + 1
print(freq)

