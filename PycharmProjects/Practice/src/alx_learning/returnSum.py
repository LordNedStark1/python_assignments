
def two_sum_index(user_input: list, target) -> list:
    new_list = []

    for i in range(len(user_input)):
        if user_input[i] < len(user_input):
            sum = user_input[i] + user_input[i + 1]

            if sum == target:
                new_list.append(i)
                new_list.append(i + 1)

    # if new_list[1] != 1 or new_list[1] < 1:
    #     sum = user_input[-1] + user_input[-2]
    #     if sum == target:
    #         new_list.append(user_input[-1])
    #         new_list.append(user_input[-2])

    return new_list


x = [1, 3, 4, 12]
target_number = 7

print(two_sum_index(x, target_number))

y = [2, 3, 6, 7]
new_target = 13
print(two_sum_index(y, new_target))


