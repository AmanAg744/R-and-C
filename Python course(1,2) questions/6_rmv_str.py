lst = ["hi","","hello",""]
for i in lst:
    if i == "":
        lst.remove("")
print(lst)