def pal(text):
    x = text[::-1]
    if text == x:
        print("Yes")
    else:
        print("No")
c = input("Введите число: ")
pal(c)