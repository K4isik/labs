import re
def snake_to_camel(s):
    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)
snake_str = input() # as form 'hsds_wosncjs_hqywt'
camel_str = snake_to_camel(snake_str)
print(camel_str)  # as form 'hsdsWosncjsHqywt'