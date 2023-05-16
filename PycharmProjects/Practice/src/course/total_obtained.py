class Student:
    def __init__(self, phy, chem, bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
        self.sum = 0

    def totalObtained(self):
        self.sum = self.phy + self.chem + self.bio

    def percentage(self):
        return ((self.sum) / 300) * 100


demo1 = Student(80, 90, 40)
demo1.totalObtained()
result = demo1.percentage()
print(result)