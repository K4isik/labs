import re
a = input() #form as "SdscTswSsdcjs"
b = re.findall('[A-Z][^A-Z]*', a)
print(b)