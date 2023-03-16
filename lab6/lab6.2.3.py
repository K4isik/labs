import os
path = input("Введите путь: ")
if os.path.exists(path):
    print("Path to directory:", os.path.dirname(path))
    print("Directory name:", os.path.basename(path))
else:
    print("Path does not exist")