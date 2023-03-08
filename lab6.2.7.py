s_file = input("Введите путь к файлу: ")
d_file = input("Введите путь ко второму файлу: ")
with open(s_file, "r") as s, open(d_file, "w") as d:
    contents = s.read()
    d.write(contents)
print("File copied successfully!")
