class Parent(object):
    def __init__(self, daddy):
        self.daddy = daddy

    def printit(self):
        print(self.daddy)


class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__(stuff)

    def printit(self):
        print(f"{self.stuff} + {self.daddy}")


d = Parent("Bo m ne con")
c = Child("huhu")
c.printit()
d.printit()
