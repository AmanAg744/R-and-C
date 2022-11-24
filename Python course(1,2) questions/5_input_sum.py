s = input()
sum = 0
for i in range(0,int((len(s)+1)/2)):
    x = int(s[2*i])
    sum = sum + x
print("Sum is",sum)