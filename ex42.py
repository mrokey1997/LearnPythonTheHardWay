# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


# ís-a
class Dog(Animal):
    def __init__(self, name):
        # has-a
        self.name = name


# is-a
class Cat(Animal):
    def __init__(self, name):
        # has-a
        self.name = name


# is-a
class Person(object):
    def __init__(self, name):
        # has-a
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# is-a
class Employee(Person):
    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # super().__init__(name)
        self.salary = salary


# employee = Employee("Bach", 12929)
# print(employee)
# print(employee.name)
# print(employee.salary)


class Butterfly:
    def __init__(self):
        self.name = "Dragon"


btf = Butterfly
btf2 = Butterfly()
print(btf2.name)


# ??
class Fish(object):
    pass


# ??
class Salmon(Fish):
    pass


# ??
class Halibut(Fish):
    pass
