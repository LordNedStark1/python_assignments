class User:
    def __init__(self, name):
        self.__name = name

    def set_name_(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

my_set = set()


# for i in range (5):
#     my_set.add(User)

user = User("john")
user1 = User("mark")
user2 = User("legend")

my_set.add(user)
my_set.add(user1)
my_set.add(user2)

matching = []
for obj in my_set:
    if obj.get_name() == "john":
        matching.append(obj)
# print(matching[0].)


