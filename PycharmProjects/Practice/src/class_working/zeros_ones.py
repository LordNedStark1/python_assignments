

def zeros(userInput):
    sum = 0
    counter = 1
    while userInput != 0 :

        if userInput % 10 == 1:
            sum += counter
            userInput //= 10

        else:
            userInput //= 10

        counter *= 2
    return sum

print(zeros(1101))