import os
path = input("Enter path to checking: ")
if os.path.exists(path):
    print(f"{path} существует")
    if os.access(path, os.R_OK):
        print(f"{path} читаемый")
    else:
        print(f"{path} не читаемый")
    if os.access(path, os.W_OK):
        print(f"{path} доступный для записи")
    else:
        print(f"{path} не доступный для записи")
    if os.access(path, os.X_OK):
        print(f"{path} исполняемый")
    else:
        print(f"{path} не исполняемый")
else:
    print(f"{path} не существует")
