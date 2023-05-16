

def add(a, b):
    return a + b

function_name = "add"
arguments = (2, 3)
result = eval(function_name)(*arguments)
print(result) # 5
add = lambda x, y: x + y
print(add(3,3))