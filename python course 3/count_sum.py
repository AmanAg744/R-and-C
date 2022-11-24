import re
f = open("sample.txt")
sum = 0
num = list()
for line in f:
    line = line.rstrip()
    num = re.findall("[0-9]+",line)
    for i in num:
        sum = sum + int(i)
print(sum)