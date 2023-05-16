def method(user_input: list):
    new_list = []
    for i in range(len(user_input) - 1, -1, -1):
        new_list.append(user_input[i])

    return new_list


def method2(user_input: list):
    return user_input[::-1]


x = [12, 3, 6, 20]
print(method2(x))
