class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The squareroot is {self.n**1/2}")
    @staticmethod
    def method():
        print("Hello! Saleh is writing a program")

calculator=Calculator(4)
calculator.square()
calculator.cube()
calculator.squareRoot()
calculator.method()