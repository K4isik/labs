import re
a = input()
con = "^a(b)*$"
if re.search(con, a):
    print('True')
else:
    print("False")