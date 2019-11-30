class Person:

    # 1) can have a property here
    x = "x"
    
    # self is a reference to current instance, must be first parameter to every method in a class
    def __init__(self, name, age):
        # 2) or can just set values to properties in self, like this
        self.name = name
        self.age = age

    __privateMember = "test"

    def getInfo(self):
        name = str(self.name)
        age = str(self.age)

        print(name+ " " + age + " " + self.__privateMember + " " + self.x)


p = Person("Adam", 55)
p.getInfo()

# Mutate state on 2 properties (1, 2)
p.x = "y"
p.name = "Bertil"
p.getInfo()



# A note on static members
# "I have my doubts as to whether emulating the static variable behavior of other languages in Python is ever actually necessary."
#   - https://stackoverflow.com/questions/68645/are-static-class-variables-possible-in-python
#
# The pythonic way for constants is to not grow a class for constants. 
# Just have some const.py with PI = 3.14 and you can import it everywhere. 
# from const import PI
#
# "use staticmethod() sparingly! There are very few situations where static-methods are necessary in Python, 
# and I've seen them used many times where a separate "top-level" function would have been clearer."
#   - https://stackoverflow.com/questions/735975/static-methods-in-python
