# class Employee:
#     def __init__(self, ID, salary):
#         self.ID = ID
#         self.__salary = salary  # salary is a private property
#
#
# Steve = Employee(3789, 2500)
# print(Steve._Employee__salary)
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x * self.x) + (self.y* self.y) +(self.z* self.z)

point = Point(1,3,5)
print (point.sqSum())