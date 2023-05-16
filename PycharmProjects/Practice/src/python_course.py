

batman = "Bruce Wayne"
manbat = batman[::-1]
print(manbat == batman)



name =  "Honesty "
other_name = " Beauty "
my_list = list(other_name.strip())

new_name = name.join( my_list)
print(new_name)



string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)

num_list = [0, 1, 2, 3, 4, 15]

double_list = map(lambda n: n > 10, num_list)

print(list(double_list))