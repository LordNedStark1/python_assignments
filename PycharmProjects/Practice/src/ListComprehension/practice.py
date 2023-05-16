

first = [i for i in range (1, 11)]
print(first)
second = [i if i % 2 == 0 else None for i in range(len( first))]

print(second)