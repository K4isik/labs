import re
def camel_to_snake(camel_str):
    snake_str = re.sub('([A-Z])', r'_\1', camel_str)
    snake_str = snake_str.lower()
    snake_str = re.sub('_+', '_', snake_str)
    if snake_str.startswith('_'):
        snake_str = snake_str[1:]
    return snake_str
camel_str =  input() #"ThisIsExample"
snake_str = camel_to_snake(camel_str)
print(snake_str)  # Output: "this_is_camel_case"