def display(my_list: list):
    for inner in my_list:
        for j in inner:
            if my_list[inner][j] == 'X':
                my_list[inner][j] = 1

            if my_list[inner][j] == 'O':
                my_list[inner][j] = 0

    return my_list


def display1(my_list: list) -> list:
    my_list = [[1 if x == 'X' else 0 if x == 'O' else x for x in row] for row in my_list]
    return my_list


result = [['O', 'X', 'O'], ['X', 'O', 'O'], ['X', 'O', 'X']]
print(display1(result))
