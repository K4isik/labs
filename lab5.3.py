import re
text = input()
pattern = r'[a-z]+_[a-z]+'
res = re.findall(pattern, text)
print(res)
