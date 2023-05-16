
my_dict = {}
my_list =[]
second_list = []


for i in range (5):
    key = input("enter a key ")
    my_list.append(i + 10)
    value = input("enter a value ")
    my_dict[key] = value
    second_list.append(value + key)


print(my_dict.items())
print(my_dict.values())
print(my_dict)

key = input("Enter a search key ")

print(my_dict.get(key))
print(my_dict.popitem())
prin = my_dict.fromkeys(my_list, "ben")
print(prin)

if my_dict.get(key) is not None:
    print(my_dict.pop(key))
print(my_dict)

key = input("Enter a search key ")
if my_dict.get(key) is not None:
    print(my_dict.pop(key))

print(my_dict)
