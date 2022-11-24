import random
s = ""
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
l = int(input())
for i in range(0,l):
     s = s + random.choice(alpha)
print(s)
