class Animals:
    pass
class Pats(Animals):
    pass
class Dog(Pats):
    @staticmethod
    def bark():
        print("Bow Bow......")

a=Dog()
a.bark()