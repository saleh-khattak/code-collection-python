class Employee:
    selary=340
    increment=5.5

    @property
    def selaryAfterIncrement(self):
        return (self.selary+self.selary *(self.increment/100))
    
    @selaryAfterIncrement.setter
    def selaryAfterIncrement(self,selary):
        self.increment=((selary/self.selary)-1)*100

e=Employee()
print(f"The salery after increament is :{e.selaryAfterIncrement}")
e.selaryAfterIncrement=360
print(f"The increment of selery is:{e.increment}")