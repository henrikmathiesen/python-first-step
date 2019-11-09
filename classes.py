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


# A note on static members
# "I have my doubts as to whether emulating the static variable behavior of other languages in Python is ever actually necessary."
#   - https://stackoverflow.com/questions/68645/are-static-class-variables-possible-in-python
#
# The pythonic way for constants is to not grow a class for constants. 
# Just have some const.py with PI = 3.14 and you can import it everywhere. 
# from const import PI
