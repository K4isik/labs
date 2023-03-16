import re
a = input()
pattern = r"[A-Z][a-z]+"
res = re.findall(pattern, a)
print(res)