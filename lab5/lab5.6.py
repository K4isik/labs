import re
a = input()
res1 = re.sub(" ", ":", a)
res1 = re.sub("[,]", ":", res1)
res1 = re.sub("[.]", ":", res1)
print(res1)