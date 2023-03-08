l = ["Real", "Kairat", "Chelsea"]
with open("fruits.txt", "w") as file:
    for i in l:
        file.write(i + "\n")