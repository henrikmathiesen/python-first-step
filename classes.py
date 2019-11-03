class Person:
    
    # self is a reference to current instance, must be first parameter to every method in a class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    __privateMember = "test"

    def getInfo(self):
        name = str(self.name)
        age = str(self.age)

        print(name+ " " + age + " " + self.__privateMember)


p = Person("Adam", 55)
p.getInfo()
