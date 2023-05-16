

def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print(result)