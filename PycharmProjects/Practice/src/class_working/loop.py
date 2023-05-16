import numbers
import sys


def sum_numbers()-> int:
    value_to_check = eval(input("Enter a number to check "))
    sum = 0
    print(sum)
    while sum < value_to_check:
        value_to_Add = eval(input("Enter an integer "))
        sum += value_to_Add
    return sum
print("The sum is " , sum_numbers())