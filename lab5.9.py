import re
def ins_s(s):
    pattern = r'(?<!^)(?=[A-Z])'
    s = re.sub(pattern, ' ', s)
    return s
s = input() # for example: 'ThereHgsabsstsisArsq'
s = ins_s(s)
print(s)  # Output: There Hgsabsstsis Arsq
