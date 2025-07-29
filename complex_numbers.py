class Complex:
    def __init__(self,i,r):
        self.i=i
        self.r=r
    
    #For addition
    def __add__(self,c2):
        return  Complex(self.r+c2.r,self.i+c2.i)
    
    #for multiplication
    def __mul__(self,c2):
        realPart=self.r*c2.r+self.i*c2.i
        imgPart=self.r*c2.i+self.i*self.r
        return Complex(realPart,imgPart)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1=Complex(3,6)
c2=Complex(5,2)
print(f"The addition is :{c1+c2}")
print(f"The multiplication is :{c1*c2}")

