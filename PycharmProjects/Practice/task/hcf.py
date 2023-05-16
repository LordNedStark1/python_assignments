

def hcf(first_value_to_check, second_value_to_check):
    storedFactors = []
    count = 2

    for i in range(first_value_to_check):
        if first_value_to_check == 0: break

        if first_value_to_check % count == 0 and second_value_to_check % count == 0:
            storedFactors.append(count)
            first_value_to_check = first_value_to_check / count
            second_value_to_check = second_value_to_check /count
        else:
            count += 1
    return storedFactors

def hcf_for_kwargs(*kwargs):
    storedKwargs  = list(kwargs)
    storedFactors = []
    sum_of_kwargs = sum(storedKwargs)
    count = 2

    for i in range (sum_of_kwargs//2):

        if first_value_to_check % count == 0 and second_value_to_check % count == 0:
            storedFactors.append(count)
            storedKwargs[i] = storedFactors[i] / count

        else:
            count += 1

    return storedFactors

# print(hcf_for_kwargs(100, 200, 1000, 40))
print(hcf(1000, 100))