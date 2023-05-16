from typing import List


def sum_list(list: List):
    sum = 0;
    for i in range(len(list)):
        sum += list[i]

    return sum

# def add(list: List)-> int:
#     return list.


my_variable = [1,2,3,4,5]
print(sum_list(my_variable))