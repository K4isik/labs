text = input("Введите строку: ")
ucnt = 0
lcnt = 0
for i in text:
    if i.isupper():
        ucnt += 1
    elif i.islower():
        lcnt += 1
print("Number of upper case letters:", ucnt)
print("Number of lower case letters:", lcnt)